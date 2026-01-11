<template>
	<div class="home-preview">




		<!-- 新闻资讯 -->
		<div id="animate_newsnews" class="news animate__animated">
			<div class="news_title_box">
				<span class="news_title">健康资讯</span>
				<span class="news_subhead">{{'news'.toUpperCase()}}</span>
			</div>
			<!-- 样式六 -->
			<div v-if="newsList.length" class="list list6 index-pv1">
				<div id="new-list-6news" class="swiper-container swiper-new-list-6">
					<div class="swiper-wrapper">
						<div class="swiper-slide animation-box" v-for="(item,index) in newsList" v-if="index<5" :key="index" @click="toDetail('newsDetail', item)">
							<img :src="baseUrl + item.picture">
							<div class="name">{{ item.title }}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{item.addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{item.name}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{item.thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{item.storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan9"></span>
								<span class="label">点击量：</span>
								<span class="text">{{item.clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
				<div class="new6-list">
					<div class="news6-title">最新动态</div>
					<div v-for="(item,index) in newsList" v-if="index<5" :key="index" @click="toDetail('newsDetail', item)" class="list-item">
						<div class="name line1">{{ item.title }}</div>
						<div class="time_item">
							<span class="icon iconfont icon-shijian21"></span>
							<span class="label">发布时间：</span>
							<span class="text">{{item.addtime.split(' ')[0]}}</span>
						</div>
						<div class="publisher_item">
							<span class="icon iconfont icon-geren16"></span>
							<span class="label">发布人：</span>
							<span class="text">{{item.name}}</span>
						</div>
						<div class="like_item">
							<span class="icon iconfont icon-zan10"></span>
							<span class="label">点赞数：</span>
							<span class="text">{{item.thumbsupnum}}</span>
						</div>
						<div class="collect_item">
							<span class="icon iconfont icon-shoucang10"></span>
							<span class="label">收藏量：</span>
							<span class="text">{{item.storeupnum}}</span>
						</div>
						<div class="view_item">
							<span class="icon iconfont icon-chakan9"></span>
							<span class="label">点击量：</span>
							<span class="text">{{item.clicknum}}</span>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('news')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo"></i>
			</div>
		</div>
		<!-- 新闻资讯 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendjiankangzhishi" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">健康知识推荐</span>
				<span class="recommend_subhead">{{'jiankangzhishi'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div class="list list18 index-pv1">
				<div class="list-body" v-if="jiankangzhishiRecommend.length">
					<div class="list-body-left">
						<div class="list-item1" @click="toDetail('jiankangzhishiDetail', jiankangzhishiRecommend[0])">
							<div class="infoBox">
								<div class="name">{{jiankangzhishiRecommend[0].zhishibiaoti}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{jiankangzhishiRecommend[0].addtime.split(' ')[0]}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏量：</span>
									<span class="text">{{jiankangzhishiRecommend[0].storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-chakan9"></span>
									<span class="label">点击量：</span>
									<span class="text">{{jiankangzhishiRecommend[0].clicknum}}</span>
								</div>
							</div>
							<div class="img">
								<img v-if="preHttp(jiankangzhishiRecommend[0].fengmian)&&preHttp2(jiankangzhishiRecommend[0].fengmian)" :src="jiankangzhishiRecommend[0].fengmian" alt="" />
								<img v-else-if="preHttp(jiankangzhishiRecommend[0].fengmian)" :src="jiankangzhishiRecommend[0].fengmian.split(',')[0]" alt="" />
								<img v-else :src="baseUrl + (jiankangzhishiRecommend[0].fengmian?jiankangzhishiRecommend[0].fengmian.split(',')[0]:'')" alt="" />
							</div>
						</div>
						<div class="list-item2" @click="toDetail('jiankangzhishiDetail', jiankangzhishiRecommend[1])">
							<div class="img">
								<img v-if="preHttp(jiankangzhishiRecommend[1].fengmian)&&preHttp2(jiankangzhishiRecommend[1].fengmian)" :src="jiankangzhishiRecommend[1].fengmian" alt="" />
								<img v-else-if="preHttp(jiankangzhishiRecommend[1].fengmian)" :src="jiankangzhishiRecommend[1].fengmian.split(',')[0]" alt="" />
								<img v-else :src="baseUrl + (jiankangzhishiRecommend[1].fengmian?jiankangzhishiRecommend[1].fengmian.split(',')[0]:'')" alt="" />
							</div>
							<div class="infoBox">
								<div class="name">{{jiankangzhishiRecommend[1].zhishibiaoti}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{jiankangzhishiRecommend[1].addtime.split(' ')[0]}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏量：</span>
									<span class="text">{{jiankangzhishiRecommend[1].storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-chakan9"></span>
									<span class="label">点击量：</span>
									<span class="text">{{jiankangzhishiRecommend[1].clicknum}}</span>
								</div>
							</div>
						</div>
					</div>
					<div class="list-body-right">
						<div class="swiper-container recommendSwiper18 recommend-list-18jiankangzhishi">
							<div class="swiper-wrapper">
								<div class="swiper-slide" v-for="(item,index) in jiankangzhishiRecommend" :key="index" v-if="index>2">
									<div class="list-item" @click="toDetail('jiankangzhishiDetail', item)">
										<div class="img">
											<img v-if="preHttp(item.fengmian)&&preHttp2(item.fengmian)" :src="item.fengmian" alt="" />
											<img v-else-if="preHttp(item.fengmian)" :src="item.fengmian.split(',')[0]" alt="" />
											<img v-else :src="baseUrl + (item.fengmian?item.fengmian.split(',')[0]:'')" alt="" />
										</div>
										<div class="infoBox">
											<div class="name">{{item.zhishibiaoti}}</div>
											<div class="time_item">
												<span class="icon iconfont icon-shijian21"></span>
												<span class="label">发布时间：</span>
												<span class="text">{{item.addtime.split(' ')[0]}}</span>
											</div>
											<div class="collect_item">
												<span class="icon iconfont icon-shoucang10"></span>
												<span class="label">收藏量：</span>
												<span class="text">{{item.storeupnum}}</span>
											</div>
											<div class="view_item">
												<span class="icon iconfont icon-chakan9"></span>
												<span class="label">点击量：</span>
												<span class="text">{{item.clicknum}}</span>
											</div>
										</div>
									</div>
								</div>
							</div>
							<div class="swiper-button-prev"></div>
							<div class="swiper-button-next"></div>
							<div class="swiper-pagination"></div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('jiankangzhishi')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				newsList: [],
				jiankangzhishiRecommend: [],



				recommendListSwiper18jiankangzhishi: null,


			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getNewsList();
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				if (this['recommendListSwiper18jiankangzhishi']) this['recommendListSwiper18jiankangzhishi'].destroy()
				setTimeout(()=>{
					this['recommendListSwiper18jiankangzhishi'] = new Swiper(".recommend-list-18jiankangzhishi", {"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"pagination":{"el":".swiper-pagination","clickable":true},"loop":false,"coverflowEffect":{"rotate":10,"stretch":10,"depth":60,"modifier":3,"slideShadows":false},"centeredSlides":true,"slidesPerView":1,"spaceBetween":0,"autoplay":false})
				},750)
			},
			async recommendIndexClick18(index, name) {
				this['recommendIndex18' + name] = index
				await this.getList()
			},

			listIndexClick11(index, name) {
				this['listIndex11' + name] = index[this['listColumn11' + name]]
				this.getList()
			},

			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendjiankangzhishi',css:'animate__'},
					{id:'animate_newsnews',css:'animate__'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getNewsList() {
				let data = {
					page: 1,
					limit: 6,
					sort: 'addtime',
					order: 'desc'
				}
				this.$http.get('news/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
					
						let options = {"observer":true,"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"observeParents":true,"loop":false,"slidesPerView":"4","speed":500,"spaceBetween":10,"autoplay":{"delay":3000,"disableOnInteraction":false}}
						options.pagination = {el:'null'}
						if(options.slidesPerView) {
							options.slidesPerView = Number(options.slidesPerView);
						}
						if(options.spaceBetween) {
							options.spaceBetween = Number(options.spaceBetween);
						}
						this.$nextTick(() => {
							new Swiper('#new-list-6news', options)
						})
					}
				});
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "jiankangzhishi/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "jiankangzhishi/autoSort2";
				}
				data = {
					page: 1,
					limit: 6,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.jiankangzhishiRecommend = res.data.data.list;
					}
				});
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		margin: 0;
		display: flex;
		width: 100%;
		flex-wrap: wrap;
		.news {
			padding: 33px 0 60px;
			margin: 0;
			background: #f8ece5;
			width: 100%;
			position: relative;
			.news_title_box {
				padding: 0 calc((100% - 1200px)/2);
				flex-direction: column;
				background: none;
				display: flex;
				width: auto;
				line-height: 44px;
				flex-wrap: wrap;
				.news_title {
					color: #000000;
					font-weight: 600;
					font-size: 22px;
				}
				.news_subhead {
					margin: 0 0 10px;
					color: #666;
					width: 100%;
					font-size: 16px;
					line-height: 1;
				}
			}
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list6 {
				border-radius: 30px;
				padding: 30px;
				box-shadow:  0px 4px 10px 0px rgba(0,0,0,0.3);
				margin: 10px auto 0;
				background: #FFFFFF;
				display: flex;
				width: 1200px;
				height: auto;
				.swiper-container {
					padding: 0;
					margin: 0;
					background: #fff;
					flex: 1;
					width: auto;
					height: auto;
					.swiper-slide {
						border: 0;
						cursor: pointer;
						border-radius: 4px;
						margin: 0 10px;
						background: linear-gradient( 136deg, #FFB4C2 60%, #8FB0FD 100%);
						font-size: 0;
						position: relative;
						img {
							border: 0;
							border-radius: 10px;
							object-fit: cover;
							width: 100%;
							height: 218px;
						}
						.name {
							padding: 0 10px;
							overflow: hidden;
							color: #fff;
							white-space: nowrap;
							background: none;
							font-size: 14px;
							line-height: 32px;
							text-overflow: ellipsis;
						}
						.time_item {
							padding: 0 10px;
							margin: 0 0 10px;
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
						.publisher_item {
							padding: 0 10px;
							display: none;
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
							padding: 0 10px;
							display: none;
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
							padding: 0 10px;
							display: none;
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
							padding: 0 10px;
							display: none;
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
					}
				}
				.new6-list {
					border: 4px solid ;
					border-radius: 5px;
					padding: 0;
					margin: 0 0 0 10px;
					background: #fff;
					border-image: linear-gradient(145deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 4 4;
					display: flex;
					width: 320px;
					flex-wrap: wrap;
					height: auto;
					.news6-title {
						border-radius: 10px;
						padding: 0 8px;
						color: #000000;
						font-weight: 400;
						display: none;
						width: 100%;
						font-size: 18px;
						line-height: 40px;
					}
					.list-item {
						cursor: pointer;
						padding: 0 10px;
						color: #959595;
						background: #fff;
						border-image:  linear-gradient(145deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 4 4;
						display: flex;
						width: 100%;
						border-width: 0  0 1px 0;
						justify-content: space-around;
						align-items: center;
						border-style: solid;
						height: auto;
						.name {
							overflow: hidden;
							color: #959595;
							white-space: nowrap;
							width: 100%;
							font-size: 14px;
							line-height: 38px;
							text-overflow: ellipsis;
						}
						.time_item {
							overflow: hidden;
							color: #fff;
							display: none;
							width: 100px;
							font-size: 14px;
							text-overflow: ellipsis;
							-webkit-box-orient: vertical;
							-webkit-line-clamp: 2;
							.icon {
								margin: 0 2px 0 0;
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.publisher_item {
							overflow: hidden;
							color: #959595;
							display: none;
							width: 100px;
							font-size: 14px;
							text-overflow: ellipsis;
							-webkit-box-orient: vertical;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.like_item {
							padding: 0 10px;
							display: none;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.collect_item {
							padding: 0 10px;
							display: none;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.view_item {
							padding: 0 10px;
							display: none;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.label {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #959595;
								font-size: 12px;
								line-height: 1.5;
							}
						}
					}
				}
				
				.swiper-button-prev {
					left: 10px;
					right: auto;
				}
				
				.swiper-button-prev::after {
					color: rgb(64, 158, 255);
				}
				
				.swiper-button-next {
					left: auto;
					right: 10px;
				}
				
				.swiper-button-next::after {
					color: rgb(64, 158, 255);
				}
			}
			.moreBtn {
				border: 0;
				border-radius: 10px;
				margin: 40px auto 0;
				top: 10px;
				background: #FADEDC;
				display: block;
				width: 140px;
				line-height: 40px;
				position: absolute;
				right: calc((100% - 1200px)/2);
				text-align: center;
				height: 40px;
				.text {
					color: #000000;
					font-weight: 400;
					font-size: 16px;
				}
				.icon {
					color: #000000;
					display: none;
					font-size: 12px;
				}
			}
		}
		.recommend {
			padding: 30px;
			background: #fff;
			width: 100%;
			.recommend_title_box {
				padding: 0 0 20px;
				margin: 0 auto;
				background: url(http://codegen.caihongy.cn/20241205/b08c6150728242b18bc30581dde4b827.png) no-repeat bottom center /   100%;
				width: 1200px;
				line-height: auto;
				text-align: center;
				.recommend_title {
					padding: 0 10px;
					margin: 0;
					color: #000000;
					font-weight: 700;
					display: inline-block;
					font-size: 32px;
					border-color: rgba(64, 158, 255,1);
					border-width: 0;
					line-height: 40px;
					border-style: solid;
				}
				.recommend_subhead {
					margin: 0 0 30px;
					color: #666;
					font-weight: 400;
					display: inline-block;
					width: 100%;
					font-size: 16px;
					line-height: 40px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1.1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list18 {
				margin: 30px auto 0;
				background: #fff;
				width: 1200px;
				font-size: 13px;
				.tab_view {
					margin: 10px auto;
					display: none;
					width: 60%;
					justify-content: center;
					.tab {
						cursor: pointer;
						border-radius: 5px;
						margin: 0 5px 10px;
						color: #333;
						background: #eee;
						display: block;
						width: 140px;
						font-size: 14px;
						line-height: 40px;
						text-align: center;
						height: 40px;
					}
					.tab:hover {
						color: #ddd;
						background: #0195df;
					}
					.tab.tabActive {
						color: #fff;
						background: #5555ff;
					}
				}
				.list-body {
					padding: 0 10px;
					display: flex;
					width: 100%;
					.list-body-left {
						margin: 0 auto 0 0;
						width: 49%;
						.list-item1 {
							cursor: pointer;
							display: flex;
							width: 100%;
							align-items: center;
							transition: all .3s;
							.infoBox {
								border: 0px solid #d2dee7;
								align-content: center;
								display: flex;
								width: 50%;
								align-items: center;
								flex-wrap: wrap;
								height: 225px;
								.name {
									overflow: hidden;
									color: #000;
									white-space: nowrap;
									width: 100%;
									font-size: 15px;
									line-height: 24px;
									text-overflow: ellipsis;
								}
								.price {
									padding: 0;
									color: #f00;
									width: 100%;
									font-size: 16px;
									line-height: 30px;
								}
								.time_item {
									border-radius: 30px;
									padding: 5px 10px;
									margin: 5px 0 0;
									color: #fff;
									background: linear-gradient(130deg, #FFB4C2 0%, #90B0FD 100%);
									display: flex;
									width: 96%;
									font-size: 12px;
									justify-content: center;
									align-items: center;
									text-align: center;
									order: 11;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.publisher_item {
									padding: 0;
									margin: 0 10px 0 0;
									color: #73AF1A;
									order: 4;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.like_item {
									padding: 0;
									margin: 0 10px 0 0;
									color: #FF6200;
									order: 3;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.collect_item {
									padding: 0;
									margin: 0 10px 0 0;
									color: #DC9D31;
									order: 2;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.view_item {
									padding: 0;
									margin: 0 10px 0 0;
									color: #BC4C3B;
									order: 1;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
							}
							.img {
								width: 50%;
								transition: all .3s;
								height: 225px;
								img {
									border-radius: 20px;
									transform: scale(1);
									object-fit: cover;
									display: block;
									width: 100%;
									transition: all .3s;
									height: 100%;
								}
							}
						}
						.list-item1:hover {
							transform: translate3d(0px, 0px, 0px);
							.infoBox {
								.name {
								}
								.price {
								}
								.time_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.publisher_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.like_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.collect_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.view_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
							}
							.img {
								overflow: hidden;
								img {
									transform: scale(1);
								}
							}
						}
						.list-item2 {
							cursor: pointer;
							display: flex;
							width: 100%;
							align-items: center;
							transition: all .3s;
							.img {
								width: 50%;
								transition: all .3s;
								height: 225px;
								img {
									border-radius: 20px;
									transform: scale(1);
									object-fit: cover;
									display: block;
									width: 100%;
									transition: all .3s;
									height: 100%;
								}
							}
							.infoBox {
								border: 0px solid #d2dee7;
								padding: 20px;
								align-content: center;
								display: flex;
								width: 50%;
								align-items: center;
								flex-wrap: wrap;
								height: 225px;
								.name {
									overflow: hidden;
									color: #000;
									white-space: nowrap;
									width: 100%;
									font-size: 15px;
									line-height: 24px;
									text-overflow: ellipsis;
								}
								.price {
									padding: 0;
									color: #f00;
									width: 100%;
									font-size: 16px;
									line-height: 30px;
								}
								.time_item {
									border-radius: 30px;
									padding: 5px 10px;
									margin: 5px 0 0;
									color: #fff;
									background: linear-gradient(130deg, #FFB4C2 0%, #90B0FD 100%);
									display: flex;
									width: 96%;
									font-size: 12px;
									justify-content: center;
									align-items: center;
									text-align: center;
									order: 11;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.publisher_item {
									padding: 0;
									margin: 0 10px 0 0;
									color: #73AF1A;
									order: 4;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.like_item {
									padding: 0;
									margin: 0 10px 0 0;
									color: #FF6200;
									order: 3;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.collect_item {
									padding: 0;
									margin: 0 10px 0 0;
									color: #DC9D31;
									order: 2;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.view_item {
									padding: 0;
									margin: 0 10px 0 0;
									color: #BC4C3B;
									order: 1;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
							}
						}
						.list-item2:hover {
							transform: translate3d(0px, 0px, 0px);
							.img {
								overflow: hidden;
								img {
									transform: scale(1);
								}
							}
							.infoBox {
								.name {
								}
								.price {
								}
								.time_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.publisher_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.like_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.collect_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
								.view_item {
									.icon {
									}
									.label {
									}
									.text {
									}
								}
							}
						}
					}
					.list-body-right {
						width: 49%;
						.list-item {
							cursor: pointer;
							border-radius: 20px;
							width: 100%;
							position: relative;
							.img {
								border-radius: 20px;
								width: 100%;
								height: 450px;
								img {
									border-radius: 20px;
									transform: scale(1);
									object-fit: cover;
									display: block;
									width: 100%;
									transition: all .3s;
									height: 100%;
								}
							}
							.infoBox {
								border-radius: 0 0 20px 20px;
								padding: 20px 20px 40px 20px;
								color: #fff;
								left: 0;
								bottom: 0;
								background: rgba(0, 0, 0, .2);
								display: flex;
								width: 100%;
								position: absolute;
								flex-wrap: wrap;
								.name {
									overflow: hidden;
									color: #fff;
									white-space: nowrap;
									width: 100%;
									font-size: 15px;
									line-height: 24px;
									text-overflow: ellipsis;
								}
								.price {
									padding: 0;
									color: #f00;
									width: 100%;
									font-size: 16px;
									line-height: 30px;
								}
								.time_item {
									padding: 0;
									margin: 5px 10px 0 0;
									order: 11;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.publisher_item {
									padding: 0;
									margin: 0 10px 0 0;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.like_item {
									padding: 0;
									margin: 0 10px 0 0;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.collect_item {
									padding: 0;
									margin: 0 10px 0 0;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
								.view_item {
									padding: 0;
									margin: 0 10px 0 0;
									.icon {
										margin: 0 2px 0 0;
										line-height: 1.5;
									}
									.label {
										line-height: 1.5;
									}
									.text {
										line-height: 1.5;
									}
								}
							}
						}
						.swiper-button-prev {
							left: 10px;
							display: none;
							right: auto;
						}
						.swiper-button-prev::after {
							color: rgb(64, 158, 255);
						}
						.swiper-button-next {
							left: auto;
							display: none;
							right: 10px;
						}
						.swiper-button-next::after {
							color: rgb(64, 158, 255);
						}
						/deep/.swiper-pagination {
							transform: translate3d(0,0,0);
							z-index: 10;
							left: 0;
							bottom: 10px;
							width: 100%;
							position: absolute;
							transition: .3s opacity;
							text-align: center;
							.swiper-pagination-bullet {
								cursor: pointer;
								border-radius: 100%;
								margin: 0 4px;
								background: #000;
								display: inline-block;
								width: 8px;
								opacity: .2;
								height: 8px;
							}
							.swiper-pagination-bullet:hover {
								background: #fff;
							}
							.swiper-pagination-bullet.swiper-pagination-bullet-active {
								background: #fff;
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0;
				border-radius: 10px;
				padding: 0;
				margin: 30px auto 20px;
				background: #FADEDC;
				display: flex;
				width: 150px;
				line-height: 48px;
				justify-content: center;
				align-items: center;
				text-align: center;
				.text {
					color: #000000;
					font-size: 15px;
				}
				.icon {
					color: #000000;
					display: none;
					font-size: 12px;
				}
			}
		}
	}
</style>
