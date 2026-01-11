#coding:utf-8
import base64, copy, logging, os, sys, time, xlrd, json, datetime, configparser
from django.http import JsonResponse
from django.apps import apps
import numbers
from django.db.models.aggregates import Count,Sum
from django.db.models import Case, When, IntegerField, F
from django.forms import model_to_dict
import requests
from util.CustomJSONEncoder import CustomJsonEncoder
from .models import healthmonitoringforecast
from util.codes import *
from util.auth import Auth
from util.common import Common
import util.message as mes
from django.db import connection
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Q
from util.baidubce_api import BaiDuBce
from .config_model import config
import pandas as pd

import joblib
import pymysql
import numpy as np
import matplotlib
matplotlib.use('Agg')  # 在导入pyplot之前设置
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
from util.configread import config_read
import os
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.metrics import mean_squared_error,accuracy_score
from sklearn.metrics import confusion_matrix
pd.options.mode.chained_assignment = None  # default='warn'

#获取当前文件路径的根目录
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbtype, host, port, user, passwd, dbName, charset,hasHadoop = config_read(os.path.join(parent_directory,"config.ini"))
#MySQL连接配置
mysql_config = {
    'host': host,
    'user':user,
    'password': passwd,
    'database': dbName,
    'port':port
}
def auto_figsize(x_data, base_width=8, base_height=6, width_per_point=0.2):
    """根据数据点数量自动调整画布宽度"""
    num_points = len(x_data)
    dynamic_width = base_width + width_per_point * num_points
    return (dynamic_width, base_height)

#获取预测可视化图表接口
def healthmonitoringforecast_forecastimgs(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, 'message': 'success'}
        # 指定目录
        directory = os.path.join(parent_directory, "templates", "upload", "healthmonitoringforecast")
        # 获取目录下的所有文件和文件夹名称
        all_items = os.listdir(directory)
        # 过滤出文件（排除文件夹）
        files = [f'upload/healthmonitoringforecast/{item}' for item in all_items if os.path.isfile(os.path.join(directory, item))]
        msg["data"] = files
        fontlist=[]
        for font in fm.fontManager.ttflist:
            fontlist.append(font.name)
        msg["message"]=fontlist
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_forecast(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")
        connection = pymysql.connect(**mysql_config)
        query = "SELECT user,gender,systolicpressure,diastolicpressure,heartrate,bloodsugar,sleepduration, healthstatus FROM healthmonitoring"
        #2.处理缺失值
        df = pd.read_sql(query, connection).dropna()
        id = req_dict.pop('id',None)
        req_dict.pop('addtime',None)
        #数据预处理
        user_encoder = LabelEncoder()
        df['user'] = user_encoder.fit_transform(df['user'])
        gender_encoder = LabelEncoder()
        df['gender'] = gender_encoder.fit_transform(df['gender'])
        systolicpressure_encoder = LabelEncoder()
        df['systolicpressure'] = systolicpressure_encoder.fit_transform(df['systolicpressure'])
        diastolicpressure_encoder = LabelEncoder()
        df['diastolicpressure'] = diastolicpressure_encoder.fit_transform(df['diastolicpressure'])
        heartrate_encoder = LabelEncoder()
        df['heartrate'] = heartrate_encoder.fit_transform(df['heartrate'])
        bloodsugar_encoder = LabelEncoder()
        df['bloodsugar'] = bloodsugar_encoder.fit_transform(df['bloodsugar'])
        sleepduration_encoder = LabelEncoder()
        df['sleepduration'] = sleepduration_encoder.fit_transform(df['sleepduration'])
        healthstatus_encoder = LabelEncoder()
        df['healthstatus'] = healthstatus_encoder.fit_transform(df['healthstatus'])
        # 特征和目标值分离
        X = df[[
        'user',
        'gender',
        'systolicpressure',
        'diastolicpressure',
        'heartrate',
        'bloodsugar',
        'sleepduration',
        ]]
        y_true = df['healthstatus']
        # 特征标准化
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        # 使用KMeans进行聚类
        kmeans = KMeans(n_clusters=y_true.nunique(), random_state=42)
        kmeans.fit(X_scaled)
        # 获取聚类结果
        y_pred = kmeans.labels_
        #模型评估
        accuracy = accuracy_score(y_true, y_pred)
        conf_matrix = confusion_matrix(y_true, y_pred)
        print("Accuracy:", accuracy)
        print("Confusion Matrix:\n", conf_matrix)
        #可视化结果
        plt.figure(figsize=(8, 6))
        plt.rcParams['font.sans-serif'] = ['SimHei'] # 使用黑体 SimHei
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
        sns.scatterplot(x=X_scaled[:, X_scaled.shape[1]-2], y=X_scaled[:, X_scaled.shape[1]-1], hue=y_pred, palette='viridis', style=y_true, s=100)
        plt.title('KMeans聚类结果')
        plt.xlabel('user')
        plt.ylabel('gender')
        plt.legend(title='Cluster')
        directory =os.path.join(parent_directory, "templates","upload","healthmonitoringforecast","km_prediction.png")
        os.makedirs(os.path.dirname(directory), exist_ok=True)
        plt.savefig(directory)
        plt.clf()
        plt.close()
        #去预测
        new_data = pd.DataFrame([req_dict])
        try:
            new_data['user'] = user_encoder.transform(new_data['user'])
        except:
            new_data['user']=[0]
        try:
            new_data['gender'] = gender_encoder.transform(new_data['gender'])
        except:
            new_data['gender']=[0]
        try:
            new_data['systolicpressure'] = systolicpressure_encoder.transform(new_data['systolicpressure'])
        except:
            new_data['systolicpressure']=[0]
        try:
            new_data['diastolicpressure'] = diastolicpressure_encoder.transform(new_data['diastolicpressure'])
        except:
            new_data['diastolicpressure']=[0]
        try:
            new_data['heartrate'] = heartrate_encoder.transform(new_data['heartrate'])
        except:
            new_data['heartrate']=[0]
        try:
            new_data['bloodsugar'] = bloodsugar_encoder.transform(new_data['bloodsugar'])
        except:
            new_data['bloodsugar']=[0]
        try:
            new_data['sleepduration'] = sleepduration_encoder.transform(new_data['sleepduration'])
        except:
            new_data['sleepduration']=[0]
        new_data = new_data[[
        'user',
        'gender',
        'systolicpressure',
        'diastolicpressure',
        'heartrate',
        'bloodsugar',
        'sleepduration',
        ]]
        new_data_scaled = scaler.transform(new_data)
        new_pred = kmeans.predict(new_data_scaled)
        # 调整预测结果以匹配实际类别
        new_pred_adjusted = new_pred
        df = pd.DataFrame(new_pred_adjusted, columns=[
            'healthstatus',
        ])
        df['healthstatus']=df['healthstatus'].astype(int)
        df['healthstatus'] = healthstatus_encoder.inverse_transform(df['healthstatus'])
        #9.创建数据库连接,将DataFrame 插入数据库
        connection_string = f"mysql+pymysql://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}"
        engine = create_engine(connection_string)
        try:
            if req_dict :
                #遍历DataFrame，并逐行更新数据库
                with engine.connect() as connection:
                    for index, row in df.iterrows():
                        sql = """
                        INSERT INTO healthmonitoringforecast (id
                        ,healthstatus
                        )
                        VALUES (%(id)s
                    ,%(healthstatus)s
                        )
                        ON DUPLICATE KEY UPDATE
                        healthstatus = VALUES(healthstatus)
                        """
                        connection.execute(sql, {'id': id
                            , 'healthstatus': row['healthstatus']
                        })
            else:
                df.to_sql('healthmonitoringforecast', con=engine, if_exists='append', index=False)
            print("数据更新成功！")
        except Exception as e:
            print(f"发生错误: {e}")
        finally:
            engine.dispose()  # 关闭数据库连接
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_register(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")


        error = healthmonitoringforecast.createbyreq(healthmonitoringforecast, healthmonitoringforecast, req_dict)
        if error is Exception or (type(error) is str and "Exception" in error):
            msg['code'] = crud_error_code
            msg['msg'] = "用户已存在,请勿重复注册!"
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_login(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")
        datas = healthmonitoringforecast.getbyparams(healthmonitoringforecast, healthmonitoringforecast, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = mes.password_error_code
            return JsonResponse(msg, encoder=CustomJsonEncoder)

        try:
            __sfsh__= healthmonitoringforecast.__sfsh__
        except:
            __sfsh__=None

        if  __sfsh__=='是':
            if datas[0].get('sfsh')!='是':
                msg['code']=other_code
                msg['msg'] = "账号已锁定，请联系管理员审核!"
                return JsonResponse(msg, encoder=CustomJsonEncoder)
                
        req_dict['id'] = datas[0].get('id')


        return Auth.authenticate(Auth, healthmonitoringforecast, req_dict)


def healthmonitoringforecast_logout(request):
    if request.method in ["POST", "GET"]:
        msg = {
            "msg": "登出成功",
            "code": 0
        }

        return JsonResponse(msg, encoder=CustomJsonEncoder)


def healthmonitoringforecast_resetPass(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}

        req_dict = request.session.get("req_dict")

        columns=  healthmonitoringforecast.getallcolumn( healthmonitoringforecast, healthmonitoringforecast)

        try:
            __loginUserColumn__= healthmonitoringforecast.__loginUserColumn__
        except:
            __loginUserColumn__=None
        username=req_dict.get(list(req_dict.keys())[0])
        if __loginUserColumn__:
            username_str=__loginUserColumn__
        else:
            username_str=username
        if 'mima' in columns:
            password_str='mima'
        else:
            password_str='password'

        init_pwd = '123456'
        recordsParam = {}
        recordsParam[username_str] = req_dict.get("username")
        records=healthmonitoringforecast.getbyparams(healthmonitoringforecast, healthmonitoringforecast, recordsParam)
        if len(records)<1:
            msg['code'] = 400
            msg['msg'] = '用户不存在'
            return JsonResponse(msg, encoder=CustomJsonEncoder)

        eval('''healthmonitoringforecast.objects.filter({}='{}').update({}='{}')'''.format(username_str,username,password_str,init_pwd))
        
        return JsonResponse(msg, encoder=CustomJsonEncoder)



def healthmonitoringforecast_session(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}

        req_dict={"id":request.session.get('params').get("id")}
        msg['data']  = healthmonitoringforecast.getbyparams(healthmonitoringforecast, healthmonitoringforecast, req_dict)[0]

        return JsonResponse(msg, encoder=CustomJsonEncoder)


def healthmonitoringforecast_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"是"})
        data=healthmonitoringforecast.getbyparams(healthmonitoringforecast, healthmonitoringforecast, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_page(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        global healthmonitoringforecast
        #当前登录用户信息
        tablename = request.session.get("tablename")

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =healthmonitoringforecast.page(healthmonitoringforecast, healthmonitoringforecast, req_dict, request)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_autoSort(request):
    '''
    ．智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
主要信息列表（如商品列表，新闻列表）中使用，显示最近点击的或最新添加的5条记录就行
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in healthmonitoringforecast.getallcolumn(healthmonitoringforecast,healthmonitoringforecast):
            req_dict['sort']='clicknum'
        elif "browseduration"  in healthmonitoringforecast.getallcolumn(healthmonitoringforecast,healthmonitoringforecast):
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = healthmonitoringforecast.page(healthmonitoringforecast,healthmonitoringforecast, req_dict)

        return JsonResponse(msg, encoder=CustomJsonEncoder)

#分类列表
def healthmonitoringforecast_lists(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":[]}
        msg['data'],_,_,_,_  = healthmonitoringforecast.page(healthmonitoringforecast, healthmonitoringforecast, {})
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_query(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        try:
            query_result = healthmonitoringforecast.objects.filter(**request.session.get("req_dict")).values()
            msg['data'] = query_result[0]
        except Exception as e:

            msg['code'] = crud_error_code
            msg['msg'] = f"发生错误：{e}"
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_list(request):
    '''
    前台分页
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        #获取全部列名
        columns=  healthmonitoringforecast.getallcolumn( healthmonitoringforecast, healthmonitoringforecast)
        if "vipread" in req_dict and "vipread" not in columns:
          del req_dict["vipread"]
        #表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
        try:
            __foreEndList__=healthmonitoringforecast.__foreEndList__
        except:
            __foreEndList__=None
        try:
            __foreEndListAuth__=healthmonitoringforecast.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        #authSeparate
        try:
            __authSeparate__=healthmonitoringforecast.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="是" and __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and request.session.get("params") is not None:
                req_dict['userid']=request.session.get("params").get("id")

        tablename = request.session.get("tablename")
        if tablename == "users" and req_dict.get("userid") != None:#判断是否存在userid列名
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "是":
                if req_dict.get("userid"):
                    # del req_dict["userid"]
                    pass
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if "userid" in columns:
                    try:
                        pass
                    except:
                        pass
        #当列属性authTable有值(某个用户表)[该列的列名必须和该用户表的登陆字段名一致]，则对应的表有个隐藏属性authTable为”是”，那么该用户查看该表信息时，只能查看自己的
        try:
            __authTables__=healthmonitoringforecast.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="是":
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    try:
                        del req_dict['userid']
                    except:
                        pass
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break
        
        if healthmonitoringforecast.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass


        q = Q()
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = healthmonitoringforecast.page(healthmonitoringforecast, healthmonitoringforecast, req_dict, request, q)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_save(request):
    '''
    后台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys():
            del req_dict['clicktime']
        tablename=request.session.get("tablename")
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        #获取全部列名
        columns=  healthmonitoringforecast.getallcolumn( healthmonitoringforecast, healthmonitoringforecast)
        if tablename!='users' and req_dict.get("userid")==None and 'userid' in columns  and __isAdmin__!='是':
            params=request.session.get("params")
            req_dict['userid']=params.get('id')


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']

        idOrErr= healthmonitoringforecast.createbyreq(healthmonitoringforecast,healthmonitoringforecast, req_dict)
        if idOrErr is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = idOrErr
        else:
            msg['data'] = idOrErr

        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_add(request):
    '''
    前台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        tablename=request.session.get("tablename")

        #获取全部列名
        columns=  healthmonitoringforecast.getallcolumn( healthmonitoringforecast, healthmonitoringforecast)
        try:
            __authSeparate__=healthmonitoringforecast.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=healthmonitoringforecast.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params").get("id")


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']
        error= healthmonitoringforecast.createbyreq(healthmonitoringforecast,healthmonitoringforecast, req_dict)
        if error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_thumbsup(request,id_):
    '''
     点赞：表属性thumbsUp[是/否]，刷表新增thumbsupnum赞和crazilynum踩字段，
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=healthmonitoringforecast.getbyid(healthmonitoringforecast,healthmonitoringforecast,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = healthmonitoringforecast.updatebyparams(healthmonitoringforecast,healthmonitoringforecast, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)


def healthmonitoringforecast_info(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = healthmonitoringforecast.getbyid(healthmonitoringforecast,healthmonitoringforecast, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= healthmonitoringforecast.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"  and  "clicknum"  in healthmonitoringforecast.getallcolumn(healthmonitoringforecast,healthmonitoringforecast):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}
            ret=healthmonitoringforecast.updatebyparams(healthmonitoringforecast,healthmonitoringforecast,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_detail(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =healthmonitoringforecast.getbyid(healthmonitoringforecast,healthmonitoringforecast, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= healthmonitoringforecast.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"   and  "clicknum"  in healthmonitoringforecast.getallcolumn(healthmonitoringforecast,healthmonitoringforecast):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}

            ret=healthmonitoringforecast.updatebyparams(healthmonitoringforecast,healthmonitoringforecast,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def healthmonitoringforecast_update(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys() and req_dict['clicktime']=="None":
            del req_dict['clicktime']
        if req_dict.get("mima") and "mima" not in healthmonitoringforecast.getallcolumn(healthmonitoringforecast,healthmonitoringforecast) :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in healthmonitoringforecast.getallcolumn(healthmonitoringforecast,healthmonitoringforecast) :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = healthmonitoringforecast.updatebyparams(healthmonitoringforecast, healthmonitoringforecast, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def healthmonitoringforecast_delete(request):
    '''
    批量删除
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=healthmonitoringforecast.deletes(healthmonitoringforecast,
            healthmonitoringforecast,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def healthmonitoringforecast_vote(request,id_):
    '''
    浏览点击次数（表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1）
统计商品或新闻的点击次数；提供新闻的投票功能
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= healthmonitoringforecast.getbyid(healthmonitoringforecast, healthmonitoringforecast, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=healthmonitoringforecast.updatebyparams(healthmonitoringforecast,healthmonitoringforecast,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)

def healthmonitoringforecast_importExcel(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        excel_file = request.FILES.get("file", "")
        if excel_file.size > 100 * 1024 * 1024:  # 限制为 100MB
            msg['code'] = 400
            msg["msg"] = '文件大小不能超过100MB'
            return JsonResponse(msg)

        file_type = excel_file.name.split('.')[1]
        
        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = data.sheets()[0]
            rows = table.nrows
            
            try:
                for row in range(1, rows):
                    row_values = table.row_values(row)
                    req_dict = {}
                    healthmonitoringforecast.createbyreq(healthmonitoringforecast, healthmonitoringforecast, req_dict)
                    
            except:
                pass
                
        else:
            msg = {
                "msg": "文件类型错误",
                "code": 500
            }
                
        return JsonResponse(msg)

def healthmonitoringforecast_autoSort2(request):
    return JsonResponse({"code": 0, "msg": '',  "data":{}})













