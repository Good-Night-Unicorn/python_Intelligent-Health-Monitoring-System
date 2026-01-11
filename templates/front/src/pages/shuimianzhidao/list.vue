<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div v-if="centerType" class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="list-preview">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="list-item">
					<el-input v-model="formSearch.yonghuxingming" placeholder="用户姓名" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-button class="list-search-btn" v-if=" true " type="primary" @click="getList(1, curFenlei)">
					<i class="el-icon-search"></i>
					查询
				</el-button>
				<el-button class="list-add-btn" v-if="btnAuth('shuimianzhidao','新增')" type="primary" @click="add('/index/shuimianzhidaoAdd')">
					<i class="el-icon-circle-plus-outline"></i>
					添加
				</el-button>
			</el-form>
			<div class="select2">
				<div class="select2-list" v-for="(item,index) in selectOptionsList" :key="index">
					<div class="label">{{item.name}}：</div>
					<div class="item-body">
						<div class="item" @click="selectClick2(item,-1)" :class="item.check ==-1 ? 'active' : ''">全部</div>
						<div class="item" @click="selectClick2(item,index1)" :class="item.check == index1 ? 'active' : ''" v-for="item1,index1 in item.list" :key="index1">{{item1}}</div>
					</div>
				</div>
			</div>
			<div class="list">
				<!-- 样式四 -->
				<div class="list list4 index-pv1">
					<div v-for="(item, index) in dataList" :key="index" @click.stop="toDetail(item)" class="list-item">
						<img @click.stop="imgPreView(item.touxiang)" v-if="item.touxiang && item.touxiang.substr(0,4)=='http'&&item.touxiang.split(',w').length>1" :src="item.touxiang" class="image" />
						<img @click.stop="imgPreView(item.touxiang.split(',')[0])" v-else-if="item.touxiang && item.touxiang.substr(0,4)=='http'" :src="item.touxiang.split(',')[0]" class="image" />
						<img @click.stop="imgPreView(baseUrl + (item.touxiang?item.touxiang.split(',')[0]:''))" v-else :src="baseUrl + (item.touxiang?item.touxiang.split(',')[0]:'')" class="image" />
						<div class="content">
							<div class="infoBox">
								<div class="name">{{item.yonghuxingming}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime}}</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

	
			<el-pagination
				background
				id="pagination"
				class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				prev-text="<"
				next-text=">"
				:hide-on-single-page="true"
				:layout='["total","prev","pager","next","sizes","jumper"].join()'
				:total="total"
				:page-sizes="pageSizes"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>
		</div>
		<el-dialog title="预览图" :visible.sync="previewVisible" width="50%">
			<img :src="previewImg" alt="" style="width: 100%;">
		</el-dialog>
	</div>
</template>
<script>
	export default {
		//数据集合
		data() {
			return {
				selectIndex2: 0,
				selectOptionsList: [],
				layouts: '',
				swiperIndex: -1,
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '睡眠指导'
					}
				],
				formSearch: {
					yonghuxingming: '',
				},
				fenlei: [],
				dataList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				curFenlei: '全部',
				isPlain: false,
				indexQueryCondition: '',
				timeRange: [],
				centerType:false,
				previewImg: '',
				previewVisible: false,
				sortType: 'id',
				sortOrder: 'desc',
			}
		},
		async created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0){
				this.centerType = true
			}
			this.baseUrl = this.$config.baseUrl;
			await this.getFenlei();
			let fenlei = '全部'
			if(this.$route.query.homeFenlei){
				fenlei = this.$route.query.homeFenlei
			}
			this.getList(1, fenlei);
		},
		watch:{
			$route(newValue){
				this.getList(1, newValue.query.homeFenlei);
			}
		},
		//方法集合
		methods: {
			selectClick2(row,index) {
				row.check = index
				if(index == -1){
					this.formSearch[row.tableName] = ''
				}else {
					this.formSearch[row.tableName] = row.list[index]
				}
				this.getList()
			},
			add(path) {
				let query = {}
				if(this.centerType){
					query.centerType = 1
				}
				this.$router.push({path: path,query:query});
			},
			async getFenlei() {
			},
			getList(page, fenlei, ref = '') {
				let params = {
					page,
					limit: this.pageSize,
				};
				let searchWhere = {};
				if (this.formSearch.yonghuxingming != '') searchWhere.yonghuxingming = '%' + this.formSearch.yonghuxingming + '%';
				let user = JSON.parse(localStorage.getItem('sessionForm'))
				if (this.sortType) searchWhere.sort = this.sortType
				if (this.sortOrder) searchWhere.order = this.sortOrder
				this.$http.get(`shuimianzhidao/${this.centerType?'page':'list'}`, {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.dataList = res.data.data.list;
						this.total = Number(res.data.data.total);
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			curChange(page) {
				this.getList(page);
			},
			prevClick(page) {
				this.getList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getList(1);
			},
			nextClick(page) {
				this.getList(page);
			},
			imgPreView(url){
				this.previewImg = url
				this.previewVisible = true
			},
			toDetail(item) {
				let params = {
					id: item.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/shuimianzhidaoDetail', query: params});
			},
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			backClick() {
				this.$router.push({path: '/index/center'});
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.list-preview {
		padding: 0 calc((100% - 1200px)/2);
		color: #333;
		background: #fafcff;
		display: flex;
		width: 100%;
		font-size: 16px;
		position: relative;
		flex-wrap: wrap;
		.list-form-pv {
			padding: 10px 0;
			margin: 10px auto;
			background: #fafcff;
			display: flex;
			width: 101%;
			align-items: center;
			flex-wrap: wrap;
			height: auto;
			.list-item {
				margin: 0 10px;
				/deep/.el-form-item__content {
					display: flex;
				}
				.el-input {
					margin: 5px ;
					width: 100%;
				}
				.datetimerange {
					border: 0;
					border-radius: 8px;
					padding: 3px 10px;
					box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.3);
					outline: none;
					background: #fff;
					width: auto;
					justify-content: center;
				}
				.el-input /deep/ .el-input__inner {
					border: 0;
					border-radius: 8px;
					padding: 0 10px;
					box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.3);
					margin: 0;
					outline: none;
					color: #333;
					width: 140px;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
				.el-select {
					box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.3);
					width: 100%;
				}
				.el-select /deep/ .el-input__inner {
				}
				.el-date-editor {
					box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.3);
					width: 100%;
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 0;
					border-radius: 8px;
					padding: 0 30px;
					box-shadow: 0px 4px 5px 0px rgba(0,0,0,0.3);
					margin: 0;
					outline: none;
					color: #333;
					width: 140px;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
			}
			.list-search-btn {
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
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: 14px;
				}
			}
			.list-add-btn {
				cursor: pointer;
				border: 0;
				border-radius: 4px;
				padding: 0px 15px;
				margin: 0 10px 0 0;
				outline: none;
				color: #fff;
				background: #90B0FD;
				width: auto;
				font-size: 14px;
				line-height: 42px;
				height: 42px;
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: 14px;
				}
			}
		}
		.select2 {
			border-radius: 0px 0px 20px 20px;
			padding: 20px;
			box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.3);
			margin: 0 0 20px 0;
			background: #fff;
			border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
			width: 100%;
			border-width: 4px 0 0 0;
			border-style: solid;
			height: auto;
			.select2-list {
				padding: 0;
				margin: 4px 0;
				background: #f5f5f5;
				display: flex;
				width: 100%;
				position: relative;
				height: auto;
				.label {
					padding: 10px ;
					color: #000000;
					white-space: nowrap;
					font-weight: 400;
					display:  inline-block;
					font-size: 14px;
					border-color: #FFB4C2;
					line-height: 32px;
					border-radius: 0;
					background: #fff;
					border-width: 0 0 1px 0;
					border-style: solid;
					text-align: right;
				}
				.item-body {
					padding: 10px 0;
					border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
					background: #fff;
					display:  inline-block;
					width: 100%;
					border-width: 0 0 1px 0;
					border-style: solid;
					flex-wrap: wrap;
					height: auto;
					.item {
						cursor: pointer;
						border-radius: 4px;
						padding: 0px 20px;
						color: #000000;
						background: none;
						display:  inline-block;
						font-size: 14px;
						line-height: 32px;
					}
					.item:hover {
						color: #fff;
						background: linear-gradient(133deg, rgb(144, 176, 253) 0%, rgb(254, 180, 194) 100%);
					}
					.item.active {
						color: #fff;
						background: linear-gradient(133deg, rgb(144, 176, 253) 0%, rgb(254, 180, 194) 100%);
						display:  inline-block;
					}
				}
			}
		}
		.list {
			margin: 20px 0 0;
			flex: 1;
			width: 100%;
			order: 6;
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
				
			.index-pv1 .animation-box:hover {
				transform: rotate(0) scale(1.2) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
				
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0) scale(0.8) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list4 {
				border-radius: 0 0 20px 20px;
				box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.3);
				padding: 10px 0 10px 10px;
				margin: 0;
				background: #fff;
				border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
				display: flex;
				width: calc(100% - 0px);
				border-width: 4px 0 0 0;
				border-style: solid;
				flex-wrap: wrap;
				height: auto;
				.list-item {
					border-radius: 10px;
					margin: 10px  ;
					overflow: hidden;
					width: calc(34% - 30px);
					position: relative;
					height: 280px;
					.image {
						object-fit: cover;
						display: block;
						width: 100%;
						transition: 0.3s;
						height: 100%;
					}
					.content {
						padding: 10px;
						left: 0;
						bottom: -100%;
						background: rgba(0,0,0,.5);
						display: flex;
						width: 100%;
						position: absolute;
						flex-wrap: wrap;
						transition: 0.3s;
						height: 100%;
						.desc {
							color: #fff;
							flex: 1;
							display: none;
							font-size: 14px;
							line-height: 21px;
						}
						.infoBox {
							padding: 0 0 0 10px;
							flex: 1;
							height: 100%;
							.name {
								color: #fff;
								width: 100%;
								font-size: 14px;
								line-height: 1.5;
							}
							.price {
								color: #FF4949;
								width: 100%;
								font-size: 18px;
								line-height: 1.5;
							}
							.time_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #FFAFA2;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFAFA2;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #FFAFA2;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #FFD285;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FFD285;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #FFD285;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #FF9757;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #FF9757;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #FF9757;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #BEFF5D;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #BEFF5D;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #BEFF5D;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
						}
					}
				}
				.list-item:hover {
					.image {
						transform: scale(1.1);
					}
					.content {
						bottom: 0;
					}
				}
			}
		}
	}
</style>
