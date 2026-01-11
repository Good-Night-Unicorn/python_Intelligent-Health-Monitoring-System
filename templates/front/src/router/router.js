import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import zhishifenleiList from '../pages/zhishifenlei/list'
import zhishifenleiDetail from '../pages/zhishifenlei/detail'
import zhishifenleiAdd from '../pages/zhishifenlei/add'
import jiankangzhishiList from '../pages/jiankangzhishi/list'
import jiankangzhishiDetail from '../pages/jiankangzhishi/detail'
import jiankangzhishiAdd from '../pages/jiankangzhishi/add'
import jiankangshujuList from '../pages/jiankangshuju/list'
import jiankangshujuDetail from '../pages/jiankangshuju/detail'
import jiankangshujuAdd from '../pages/jiankangshuju/add'
import yinshijianyiList from '../pages/yinshijianyi/list'
import yinshijianyiDetail from '../pages/yinshijianyi/detail'
import yinshijianyiAdd from '../pages/yinshijianyi/add'
import yundongjihuaList from '../pages/yundongjihua/list'
import yundongjihuaDetail from '../pages/yundongjihua/detail'
import yundongjihuaAdd from '../pages/yundongjihua/add'
import jiankangpingguList from '../pages/jiankangpinggu/list'
import jiankangpingguDetail from '../pages/jiankangpinggu/detail'
import jiankangpingguAdd from '../pages/jiankangpinggu/add'
import shuimianzhidaoList from '../pages/shuimianzhidao/list'
import shuimianzhidaoDetail from '../pages/shuimianzhidao/detail'
import shuimianzhidaoAdd from '../pages/shuimianzhidao/add'
import healthmonitoringList from '../pages/healthmonitoring/list'
import healthmonitoringDetail from '../pages/healthmonitoring/detail'
import healthmonitoringAdd from '../pages/healthmonitoring/add'
import healthmonitoringforecastList from '../pages/healthmonitoringforecast/list'
import healthmonitoringforecastDetail from '../pages/healthmonitoringforecast/detail'
import healthmonitoringforecastAdd from '../pages/healthmonitoringforecast/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'zhishifenlei',
					component: zhishifenleiList
				},
				{
					path: 'zhishifenleiDetail',
					component: zhishifenleiDetail
				},
				{
					path: 'zhishifenleiAdd',
					component: zhishifenleiAdd
				},
				{
					path: 'jiankangzhishi',
					component: jiankangzhishiList
				},
				{
					path: 'jiankangzhishiDetail',
					component: jiankangzhishiDetail
				},
				{
					path: 'jiankangzhishiAdd',
					component: jiankangzhishiAdd
				},
				{
					path: 'jiankangshuju',
					component: jiankangshujuList
				},
				{
					path: 'jiankangshujuDetail',
					component: jiankangshujuDetail
				},
				{
					path: 'jiankangshujuAdd',
					component: jiankangshujuAdd
				},
				{
					path: 'yinshijianyi',
					component: yinshijianyiList
				},
				{
					path: 'yinshijianyiDetail',
					component: yinshijianyiDetail
				},
				{
					path: 'yinshijianyiAdd',
					component: yinshijianyiAdd
				},
				{
					path: 'yundongjihua',
					component: yundongjihuaList
				},
				{
					path: 'yundongjihuaDetail',
					component: yundongjihuaDetail
				},
				{
					path: 'yundongjihuaAdd',
					component: yundongjihuaAdd
				},
				{
					path: 'jiankangpinggu',
					component: jiankangpingguList
				},
				{
					path: 'jiankangpingguDetail',
					component: jiankangpingguDetail
				},
				{
					path: 'jiankangpingguAdd',
					component: jiankangpingguAdd
				},
				{
					path: 'shuimianzhidao',
					component: shuimianzhidaoList
				},
				{
					path: 'shuimianzhidaoDetail',
					component: shuimianzhidaoDetail
				},
				{
					path: 'shuimianzhidaoAdd',
					component: shuimianzhidaoAdd
				},
				{
					path: 'healthmonitoring',
					component: healthmonitoringList
				},
				{
					path: 'healthmonitoringDetail',
					component: healthmonitoringDetail
				},
				{
					path: 'healthmonitoringAdd',
					component: healthmonitoringAdd
				},
				{
					path: 'healthmonitoringforecast',
					component: healthmonitoringforecastList
				},
				{
					path: 'healthmonitoringforecastDetail',
					component: healthmonitoringforecastDetail
				},
				{
					path: 'healthmonitoringforecastAdd',
					component: healthmonitoringforecastAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
