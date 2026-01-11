<template>
	<div>
	<!--  -->
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="''">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/newstype?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item3"><a href="javascript:void(0);">详情</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="detail-preview">
			<div class="attr">
				<div class="info">
					<div class="title-item">
						<div class="detail-title">
						</div>
					</div>
					<div class="item">
						<div class="lable">分类名称</div>
						<div class="text "  >{{detail.typename}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('newstype','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('newstype','删除')" @click="delClick">删除</el-button>
					</div>
				</div>
			</div>
		
			<div class="swiper3" v-if="detailBanner.length">
				<div class="big">
					<img id="big" :src="swiperBigUrl" class="image">
				</div>
				<div class="samll">
					<div class="swiper3-small-item" v-for="item in detailBanner" :key="item.id">
						<img v-if="item.substr(0,4)=='http'" :src="item" @click="swiperClick3(item)" class="image">
						<img v-else :src="baseUrl + item" @click="swiperClick3(baseUrl + item)" class="image">
					</div>
				</div>
			</div>


		

			<el-tabs class="detail-tabs" v-model="activeName" type="border-card" v-if="tabsNum>0" >
			</el-tabs>

		</div>
	</div>
</template>

<script>
	import axios from 'axios'
	import Swiper from "swiper";
	export default {
		//数据集合
		data() {
			return {
				tablename: 'newstype',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '健康资讯分类'
					}
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				tabsNum: 0,
				activeName: 'first',
				total: 1,
				pageSize: 10,
				totalPage: 1,
				buynumber: 1,
				centerType: false,
				storeupType: false,
				swiperBigUrl: null,
			}
		},
		created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0) {
				this.centerType = true
			}
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			
			this.init();
		},
		mounted() {
		},
		//方法集合
		methods: {
			swiperClick3(src) {
				this.swiperBigUrl = src
			},
			init() {
				this.id = this.$route.query.id
				this.baseUrl = this.$config.baseUrl;
				this.$http.get(this.tablename + '/detail/'  + this.id, {}).then(res => {
					if (res.data.code == 0) {
						this.detail = res.data.data;
						this.$forceUpdate();
						if(localStorage.getItem('frontToken')){
						}

					}
					if (this.detailBanner.length) {
						if (this.detailBanner[0].substr(0,4)=='http') {
							this.swiperBigUrl = this.detailBanner[0]
						} else {
							this.swiperBigUrl = this.baseUrl + this.detailBanner[0]
						}
					}
				});
			},
			curChange(page) {
				this.getDiscussList(page);
			},
			prevClick(page) {
				this.getDiscussList(page);
			},
			nextClick(page) {
				this.getDiscussList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getDiscussList(1);
			},
			// 返回按钮
			backClick(){
				if(this.storeupType){
					history.back()
				}else{
					let params = {}
					if(this.centerType){
						params.centerType = 1
					}
					this.$router.push({path: '/index/newstype', query: params});
				}
			},
			// 下载
			download(file ){
				if(!file) {
					this.$message({
						type: 'error',
						message: '文件不存在',
						duration: 1500,
					});
					return;
				}
				let arr = file.replace(new RegExp('upload/', "g"), "")
				axios.get(this.baseUrl + '/file/download?fileName=' + arr, {
					headers: {
						token: localStorage.getItem("frontToken")
					},
					responseType: "blob"
				}).then(({
					data
				}) => {
					const binaryData = [];
					binaryData.push(data);
					const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
						type: 'application/pdf;chartset=UTF-8'
					}))
					const a = document.createElement('a')
					a.href = objectUrl
					a.download = arr
					// a.click()
					// 下面这个写法兼容火狐
					a.dispatchEvent(new MouseEvent('click', {
						bubbles: true,
						cancelable: true,
						view: window
					}))
					window.URL.revokeObjectURL(data)
				},err=>{
					axios.get((location.href.split(this.$config.name).length>1 ? location.href.split(this.$config.name)[0] :'') + this.$config.name + '/file/download?fileName=' + arr, {
						headers: {
							token: localStorage.getItem("frontToken")
						},
						responseType: "blob"
					}).then(({
						data
					}) => {
						const binaryData = [];
						binaryData.push(data);
						const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
							type: 'application/pdf;chartset=UTF-8'
						}))
						const a = document.createElement('a')
						a.href = objectUrl
						a.download = arr
						// a.click()
						// 下面这个写法兼容火狐
						a.dispatchEvent(new MouseEvent('click', {
							bubbles: true,
							cancelable: true,
							view: window
						}))
						window.URL.revokeObjectURL(data)
					})
				})
			},


			// 权限判断
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			// 修改
			editClick(){
				this.$router.push(`/index/newstypeAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此健康资讯分类？') .then(_ => {
					this.$http.post('newstype/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									history.back()
								}
							});
						}
					});
				}).catch(_ => {});
			},
		},
		components: {
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.detail-preview {
		padding: 0 calc((100% - 1200px)/2);
		color: #333;
		align-content: flex-start;
		background: #fafcff;
		display: flex;
		width: 100%;
		font-size: 16px;
		align-items: flex-start;
		position: relative;
		flex-wrap: wrap;
		.attr {
			padding: 0;
			box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.3);
			margin: 0px  auto 20px  0;
			background: #FFFFFF;
			border-image: linear-gradient(89deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 1 1;
			flex: 1;
			display: flex;
			width: calc(50% - 20px);
			border-width: 6px 0 0 0;
			position: relative;
			border-style: solid;
			order: 1;
			.info {
				padding: 0 10px;
				margin: 0;
				flex: 1;
				.title-item {
					padding: 10px;
					margin: 0 0 0px 0;
					font-weight: 500;
					display: flex;
					font-size: 30px;
					justify-content: space-between;
					align-items: center;
					.detail-title {
						color: #000000;
						font-size: 16px;
					}
				}
				.item {
					padding: 6px 5px ;
					margin: 0;
					display: flex;
					justify-content: spaceBetween;
					.lable {
						padding: 0 10px;
						color: #9E9E9E;
						white-space: nowrap;
						font-weight: 400;
						width: auto;
						font-size: 14px;
						line-height: 24px;
						text-align: left;
						height: auto;
					}
					.text {
						padding: 0 10px;
						color: #000000;
						word-break: break-all;
						flex: 1;
						font-size: 14px;
						line-height: 24px;
						height: auto;
					}
					.price {
						color: #f00;
					}
					.bold {
						font-weight: bold;
					}
					.link {
						cursor: pointer;
						text-decoration: underline;
					}
				}
				.btn_box {
					padding: 10px 0;
					display: flex;
					flex-wrap: wrap;
				}
				.editBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: #FF8299;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.editBtn:hover {
					background: rgba(64, 158, 255, 0.5);
				}
				.delBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 10px;
					margin: 0 5px 0 0;
					outline: none;
					color: #fff;
					background: #4B7BED;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.delBtn:hover {
					background: rgba(255, 0, 0, 0.5);
				}
			}
		}
		.swiper3 {
			margin: 0 20px 0 0;
			overflow: hidden;
			display: flex;
			width: 50%;
			flex-wrap: wrap;
			height: auto;
			.big {
				border: 0;
				margin: 0;
				background: #fff;
				width: 100%;
				position: relative;
				height: 520px;
				img {
					box-shadow: 0 1px 8px rgba(0,0,0,.3);
					z-index: 1;
					top: 10px;
					left: 10px;
					object-fit: cover;
					display: block;
					width: 100%;
					position: absolute;
					height: 100%;
				}
			}
			.samll {
				padding: 0;
				margin: 20px 0 0;
				background: #fff;
				display: flex;
				width: 100%;
				height: 100px;
				.swiper3-small-item {
					margin: 0 5px;
					background: #fff;
					width: calc(25% - 10px);
					position: relative;
					height: 100%;
					img {
						box-shadow: 0 1px 8px rgba(0,0,0,.2);
						z-index: 1;
						top: 5px;
						left: 5px;
						object-fit: cover;
						display: block;
						width: 100%;
						position: absolute;
						height: 100%;
					}
				}
			}
		}
		.detail-tabs {
			padding: 30px;
			margin: 30px  0;
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
			order: 3;
			& /deep/ .el-tabs__header .el-tabs__nav-wrap {
				margin-bottom: 0;
			}
			/deep/ .el-tabs__header {
				border-radius: 30px;
				padding: 10px 20px 0 20px;
				margin: 0;
				background: #90B0FD;
				border-color: #E4E7ED;
				border-width: 0 0 0px 0;
				border-style: solid;
			}
			
			/deep/ .el-tabs__header .el-tabs__item {
				border: 0;
				padding: 0 20px;
				margin: 0;
				color: #000000;
				font-weight: 500;
				display: inline-block;
				font-size: 14px;
				line-height: 40px;
				background: transparent;
				position: relative;
				list-style: none;
				text-align: center;
				min-width: 100px;
				height: 40px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item:hover {
				border: 0;
				color: #000000;
				background: url(http://codegen.caihongy.cn/20250208/b9a823236e3b40dcbc11eb9da85cf983.png) no-repeat center bottom / 100% 100%;
			}
			
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				border: 0;
				color: #000000;
				background: url(http://codegen.caihongy.cn/20250208/b9a823236e3b40dcbc11eb9da85cf983.png) no-repeat center bottom / 100% 100%;
				min-width: 100px;
				text-align: center;
			}
			
			/deep/ .el-tabs__content {
				padding: 15px;
			}
		}
	}
</style>
