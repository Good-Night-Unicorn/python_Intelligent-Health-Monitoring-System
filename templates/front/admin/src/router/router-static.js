import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
	import news from '@/views/modules/news/list'
	import yinshijianyi from '@/views/modules/yinshijianyi/list'
	import shuimianzhidao from '@/views/modules/shuimianzhidao/list'
	import jiankangshuju from '@/views/modules/jiankangshuju/list'
	import healthmonitoring from '@/views/modules/healthmonitoring/list'
	import jiankangzhishi from '@/views/modules/jiankangzhishi/list'
	import zhishifenlei from '@/views/modules/zhishifenlei/list'
	import yonghu from '@/views/modules/yonghu/list'
	import healthmonitoringforecast from '@/views/modules/healthmonitoringforecast/list'
	import config from '@/views/modules/config/list'
	import jiankangpinggu from '@/views/modules/jiankangpinggu/list'
	import yundongjihua from '@/views/modules/yundongjihua/list'
	import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
	path: '/',
	name: '系统首页',
	component: Index,
	children: [{
		// 这里不设置值，是把main作为默认页面
		path: '/',
		name: '系统首页',
		component: Home,
		meta: {icon:'', title:'center', affix: true}
	}, {
		path: '/updatePassword',
		name: '修改密码',
		component: UpdatePassword,
		meta: {icon:'', title:'updatePassword'}
	}, {
		path: '/pay',
		name: '支付',
		component: pay,
		meta: {icon:'', title:'pay'}
	}, {
		path: '/center',
		name: '个人信息',
		component: center,
		meta: {icon:'', title:'center'}
	}
	,{
		path: '/news',
		name: '健康资讯',
		component: news
	}
	,{
		path: '/yinshijianyi',
		name: '饮食建议',
		component: yinshijianyi
	}
	,{
		path: '/shuimianzhidao',
		name: '睡眠指导',
		component: shuimianzhidao
	}
	,{
		path: '/jiankangshuju',
		name: '健康数据',
		component: jiankangshuju
	}
	,{
		path: '/healthmonitoring',
		name: '健康检测',
		component: healthmonitoring
	}
	,{
		path: '/jiankangzhishi',
		name: '健康知识',
		component: jiankangzhishi
	}
	,{
		path: '/zhishifenlei',
		name: '知识分类',
		component: zhishifenlei
	}
	,{
		path: '/yonghu',
		name: '用户',
		component: yonghu
	}
	,{
		path: '/healthmonitoringforecast',
		name: '预测信息',
		component: healthmonitoringforecast
	}
	,{
		path: '/config',
		name: '轮播图管理',
		component: config
	}
	,{
		path: '/jiankangpinggu',
		name: '健康评估',
		component: jiankangpinggu
	}
	,{
		path: '/yundongjihua',
		name: '运动计划',
		component: yundongjihua
	}
	,{
		path: '/newstype',
		name: '健康资讯分类',
		component: newstype
	}
	]
	},
	{
		path: '/login',
		name: 'login',
		component: Login,
		meta: {icon:'', title:'login'}
	},
	{
		path: '/register',
		name: 'register',
		component: register,
		meta: {icon:'', title:'register'}
	},
	{
		path: '*',
		component: NotFound
	}
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
	mode: 'hash',
	/*hash模式改为history*/
	routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}
export default router;
