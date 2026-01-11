<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
	
		<div class="news-preview-pv">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="search-item">
					<el-input v-model="title" placeholder="标题"></el-input>
				</el-form-item>
				<el-button class="search-btn" type="primary" @click="getNewsList(1)">
					<span class="icon iconfont icon-chakan14"></span>
					搜索
				</el-button>
			</el-form>
			
			<!-- category -->
			<div class="category-list">
				<div class="item" @click="categoryClick(0)" :class="categoryIndex == 0 ? 'active' : ''">全部</div>
				<div v-for="(item,index) in categoryList" @click="categoryClick(index+1)" :key="index" class="item" :class="categoryIndex == index+1 ? 'active' : ''">{{item.typename}}</div>
			</div>
			<!-- 样式七 -->
			<div class="list7 index-pv1">
				<div v-for="item in newsList" :key="item.id" @click="toNewsDetail(item)" class="list-item animation-box">
					<div class="name">{{item.title}}</div>
					<div class="desc">{{item.introduction}}</div>
					<div class="time_item">
						<span class="icon iconfont icon-shijian21"></span>
						<span class="label">发布时间:</span>
						<span class="text">{{item.addtime.split(' ')[0]}}</span>
					</div>
					<div class="publisher_item">
						<span class="icon iconfont icon-geren16"></span>
						<span class="label">发布人:</span>
						<span class="text">{{item.name}}</span>
					</div>
					<div class="like_item">
						<span class="icon iconfont icon-zan10"></span>
						<span class="label">点赞数:</span>
						<span class="text">{{item.thumbsupnum}}</span>
					</div>
					<div class="collect_item">
						<span class="icon iconfont icon-shoucang10"></span>
						<span class="label">收藏量:</span>
						<span class="text">{{item.storeupnum}}</span>
					</div>
					<div class="view_item">
						<span class="icon iconfont icon-chakan9"></span>
						<span class="label">点击量:</span>
						<span class="text">{{item.clicknum}}</span>
					</div>
					<div class="tags">新闻动态</div>
				</div>
			</div>
		
			<el-pagination
				background
				id="pagination" class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				:page-sizes="pageSizes"
				prev-text="<"
				next-text=">"
				:hide-on-single-page="true"
				:layout='["total","prev","pager","next","sizes","jumper"].join()'
				:total="total"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>

			<!-- 热门信息 -->
			<div class="hot">
				<div class="hot-title">热门信息</div>
				<div class="hot-list">
					<div class="hot-item" v-for="item in hotList" :key="item.id" @click="toNewsDetail(item)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="hot-name">{{ item.title }}</div>
						<div class="hot-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
			<!-- 最新动态 -->
			<div class="news">
				<div class="news-title">最新动态</div>
				<div class="news-list">
					<div class="news-item" v-for="item in recommendList" :key="item.id" @click="toNewsDetail(item)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="news-name">{{ item.title }}</div>
						<div class="news-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		//数据集合
		data() {
			return {
				baseUrl: this.$config.baseUrl,
				breadcrumbItem: [
				  {
					name: '健康资讯'
				  }
				],
				newsList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				layouts: '',
				title: '',
				categoryIndex: 0,
				categoryList: [],
				hotList: [],
				recommendList: [],
			}
		},
		created() {
			this.getCategoryList()
			
			this.getHotList()
			this.getRecommendList()
		},
		watch:{
			$route(newValue){
				this.getCategoryList()
			}
		},
		//方法集合
		methods: {
			getCategoryList(){
				this.$http.get('newstype/list', {params: {sort: 'typename',order: 'desc'}}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data.list;
						if(this.$route.query.homeFenlei){
							for(let i=0;i<this.categoryList.length;i++) {
								if(this.$route.query.homeFenlei == this.categoryList[i].typename) {
									this.categoryIndex = i + 1;
									const currentRoute = this.$route;
									const routeWithoutQuery = { ...currentRoute };
									delete routeWithoutQuery.query;
									this.$router.replace(routeWithoutQuery)
									break;
								}
							}
						}
						this.getNewsList(1);
					}
				});
			},
			categoryClick(index) {
				this.categoryIndex = index
				this.getNewsList()
			},
			getNewsList(page) {
				let params = {page, limit: this.pageSize,sort:'addtime',order:'desc'};
				let searchWhere = {};
				if(this.title != '') searchWhere.title = '%' + this.title + '%';
				if(this.categoryIndex!=0){
					searchWhere.typename = this.categoryList[this.categoryIndex - 1].typename
				}
				this.$http.get('news/list', {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			getHotList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.hotList = res.data.data.list;
					}
				});
			},
			getRecommendList(){
				let url = 'news/autoSort'
				if(localStorage.getItem('frontToken')){
					url = 'news/autoSort2'
				}
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get(url, {params: params}).then(res => {
					if (res.data.code == 0) {
						this.recommendList = res.data.data.list;
					}
				});
			},
			curChange(page) {
				this.getNewsList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getNewsList(1);
			},
			prevClick(page) {
				this.getNewsList(page);
			},
			nextClick(page) {
				this.getNewsList(page);
			},
			toNewsDetail(item) {
				this.$router.push({path: '/index/newsDetail', query: {id: item.id}});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.news-preview-pv {
				padding: 0;
				color: #333;
				background: #fafcff;
				display: flex;
				width: 100%;
				font-size: 16px;
				justify-content: flex-start;
				align-items: flex-start;
				position: relative;
				flex-wrap: wrap;
				.list-form-pv {
						padding: 10px;
						margin: 0 auto;
						display: flex;
						width: 1200px ;
						justify-content: center;
						align-items: center;
						height: auto;
						.search-item {
								margin: 0 10px;
								.el-input {
										width: 100%;
									}
				.el-input /deep/ .el-input__inner {
										border: 1px solid #eee;
										border-radius: 8px;
										padding: 0 10px;
										margin: 0;
										outline: none;
										color: #333;
										width: 400px;
										font-size: 14px;
										line-height: 42px;
										height: 42px;
									}
			}
			.search-btn {
								cursor: pointer;
								border: 0;
								border-radius: 4px;
								padding: 0px 15px;
								margin: 0 10px 0 0;
								outline: none;
								color: #fff;
								background: #FEB4C2;
								width: auto;
								font-size: 14px;
								line-height: 42px;
								height: 42px;
								.icon {
										margin: 0 10px 0 0;
										color: #fff;
										font-size: 14px;
									}
			}
		}
		.category-list {
						padding: 10px ;
						margin: 0 auto;
						display: flex;
						width: 1200px ;
						height: auto;
						.item {
								cursor: pointer;
								border-radius: 0;
								margin: 0 10px 0 0;
								color: #9E9E9E;
								background: none;
								width: 72px;
								font-size: 14px;
								border-color: #D8D8D8;
								border-width: 0 0 1px 0;
								line-height: 36px;
								border-style: solid;
								text-align: center;
							}
			
			.item:hover {
								color: #000000;
								background: none;
								border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
								border-width: 0 0 2px 0;
								border-style: solid;
							}
			
			.item.active {
								color: #000000;
								background: none;
								border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
								border-width: 0 0 2px 0;
								border-style: solid;
							}
		}
		.list7 {
						margin: 10px auto 0;
						display: flex;
						width: 1200px;
						justify-content: space-between;
						flex-wrap: wrap;
						height: auto;
						.list-item {
								cursor: pointer;
								border-radius: 0 0 20px 20px;
								padding: 10px 20px;
								box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.3);
								margin: 10px 0;
								background: #fff;
								border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
								width: calc(50% - 10px);
								border-width: 6px 0 0 0 ;
								position: relative;
								border-style: solid;
								height: auto;
								.name {
										overflow: hidden;
										color: #000000;
										white-space: nowrap;
										font-weight: 700;
										width: 100%;
										font-size: 15px;
										line-height: 32px;
										text-overflow: ellipsis;
									}
				.desc {
										color: #878787;
										width: 100%;
										font-size: 14px;
										line-height: 21px;
									}
				.time_item {
										padding: 0 10px 0 0;
										display: inline-block;
										order: 11;
										.icon {
												margin: 0 2px 0 0;
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.publisher_item {
										padding: 0 10px 0 0;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.like_item {
										padding: 0 10px 0 0;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.collect_item {
										padding: 0 10px 0 0;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.view_item {
										padding: 0 10px 0 0;
										display: inline-block;
										.icon {
												margin: 0 2px 0 0;
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.label {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
					.text {
												color: #666;
												font-size: 12px;
												line-height: 1.5;
											}
				}
				.tags {
										padding: 0 10px;
										margin: 10px 0;
										color: #fff;
										background: linear-gradient( 134deg, #90B0FD 0%, #FFB4C2 100%);
										display: block;
										width: 80px;
										font-size: 14px;
										line-height: 32px;
										text-align: center;
									}
			}
		}
		.hot {
						padding: 30px;
						margin: 30px  auto;
						border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
						flex-wrap: wrap;
						border-radius: 0px  0px  20px  20px;
						box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.3);
						background: #FFFFFF;
						width: 1200px;
						justify-content: space-between;
						border-width: 6px 0 0 0;
						border-style: solid;
						height: auto;
						order: 60;
						.hot-title {
								padding: 0 0 10px 0;
								margin: 10px auto;
								font-weight: 700;
								width: 100%;
								font-size: 23px;
								line-height: 54px;
								text-align: center;
							}
			.hot-list {
								display: flex;
								width: 100%;
								justify-content: space-between;
								position: relative;
								height: auto;
								.hot-item {
										cursor: pointer;
										background: none;
										display: block;
										width: 23%;
										position: relative;
										flex-wrap: wrap;
										height: 150px;
										img {
												border-radius: 5px;
												object-fit: cover;
												display: block;
												width: 48%;
												float: left;
												height: 120px;
											}
					.hot-name {
												padding: 0;
												margin: 0;
												overflow: hidden;
												color: #000000;
												white-space: nowrap;
												width: 49%;
												font-size: 16px;
												line-height: 24px;
												text-overflow: ellipsis;
												float: right;
												text-align: center;
											}
					.hot-time {
												padding: 0;
												margin: 0;
												color: #90B0FD;
												border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
												font-size: 14px;
												line-height: 30px;
												float: right;
												background: none;
												width: 49%;
												border-width: 0 0 2px 0;
												border-style: solid;
												text-align: center;
												height: auto;
											}
				}
			}
		}
		.news {
						padding: 10px 30px 30px;
						margin: 30px  auto;
						border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
						flex-wrap: wrap;
						border-radius: 0px  0px  20px  20px;
						box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.3);
						background: #FFFFFF;
						width: 1200px;
						justify-content: space-between;
						border-width: 6px 0 0 0;
						border-style: solid;
						height: auto;
						order: 60;
						.news-title {
								padding: 0 0 0px 0;
								margin: 10px auto;
								font-weight: 700;
								width: 100%;
								font-size: 23px;
								line-height: 54px;
								text-align: center;
							}
			.news-list {
								padding: 0px 20px 20px;
								background: #fff;
								display: flex;
								width: 100%;
								justify-content: space-between;
								height: auto;
								.news-item {
										border: 20px solid;
										border-radius: 30px  0px  30px  0px;
										padding: 20px;
										background: #fff;
										border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
										width: 23%;
										height: auto;
										img {
												border-radius: 5px;
												object-fit: cover;
												display: block;
												width: 100%;
												height: 120px;
											}
					.news-name {
												padding: 0;
												overflow: hidden;
												white-space: nowrap;
												width: 100%;
												font-size: 16px;
												line-height: 24px;
												text-overflow: ellipsis;
											}
					.news-time {
												padding: 0;
												color: #90B0FD;
												font-size: 14px;
												line-height: 24px;
											}
				}
			}
		}
	}
	
	.index-pv1 .animation-box {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		z-index: initial;
	}
	
	.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, -5px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
	}
	
	.index-pv1 .animation-box img {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
	}
	
	.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(0.8) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
</style>
