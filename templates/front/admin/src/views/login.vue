<template>
	<div>
		<div class="login-container">
			<div class="login-swiper3">
				<div class="swiper-container mySwiper3">
					<div class="swiper-wrapper">
						<div class="swiper-slide" v-for="(item,index) in swiperList" :key="item.id">
							<div>
								<el-image :src="item.url" fit="cover"></el-image>
							</div>
						</div>
					</div>
					<!-- Add Pagination -->
					<div class="swiper-pagination"></div>
					<!-- Add Arrows -->
					<div class="swiper-button-next">
						<span class="icon iconfont icon-jiantou18"></span>
					</div>
					<div class="swiper-button-prev">
						<span class="icon iconfont icon-jiantou39"></span>
					</div>
				</div>
			</div>
			<el-form class="login_form animate__animated animate__backInDown">
				<div class="login_form2">
					<div class="title-container">智能健康检测系统设计与实现</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							账号：
						</div>
						<input placeholder="请输入账号：" name="username" type="text" v-model="rulesForm.username">
					</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							密码：
						</div>
						<div class="password-box">
							<input placeholder="请输入密码：" name="password" :type="showPassword?'text':'password'" v-model="rulesForm.password">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item " v-if="roles.length>1">
						<div class="lable">
							角色：
						</div>
						<div prop="loginInRole" class="list-type">
							<el-radio v-if="loginType==1||(loginType==2&&item.roleName!='管理员')" v-for="item in roles" v-bind:key="item.roleName" v-model="rulesForm.role" :label="item.roleName">{{item.roleName}}</el-radio>
						</div>
					</div>

		
					<div class="login-btn">
						<div class="login-btn1">
							<el-button v-if="loginType==1" type="primary" @click="login()" class="loginInBt">登录</el-button>
						</div>
						<div class="login-btn2">
						</div>
						<div class="login-btn3">
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>
<script>
	import 'animate.css'
	import menu from "@/utils/menu";
	import Swiper from "swiper";
	export default {
		data() {
			return {
				verifyCheck2: false,
				flag: false,
				baseUrl:this.$base.url,
				loginType: 1,
				rulesForm: {
					username: "",
					password: "",
					role: "",
				},
				menus: [],
				roles: [],
				tableName: "",
				showPassword: false,
				swiperList: [{"name":"003.jpg","uid":1728616849394,"url":"http://codegen.caihongy.cn/20241011/cdd202eb0b26409ab20c5e573dd24894.jpg","status":"success"},{"name":"001.jpg","uid":1728616855350,"url":"http://codegen.caihongy.cn/20241011/7a9f672e2d62403b8e7a3014f354aa5a.jpg","status":"success"},{"name":"002.jpg","uid":1728616858212,"url":"http://codegen.caihongy.cn/20241011/65d8b29acea54c95b075c36f7fcfd88a.jpg","status":"success"}],
			};
		},
		mounted() {
			let menus = menu.list();
			this.menus = menus;

			for (let i = 0; i < this.menus.length; i++) {
				if (this.menus[i].hasBackLogin=='是') {
					this.roles.push(this.menus[i])
				}
			}

			setTimeout(()=>{
				new Swiper(".mySwiper3", {"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"pagination":{"el":".swiper-pagination","clickable":true},"autoplay":{"delay":3000,"disableOnInteraction":false},"effect":"fade"})
			}, 500)
		},
		created() {

		},
		destroyed() {
		},
		components: {
		},
		methods: {

			//注册
			register(tableName){
				this.$storage.set("loginTable", tableName);
				this.$router.push({path:'/register',query:{pageFlag:'register'}})
			},
			// 登陆
			login() {

				if (!this.rulesForm.username) {
					this.$message.error("请输入用户名");
					return;
				}
				if (!this.rulesForm.password) {
					this.$message.error("请输入密码");
					return;
				}
				if(this.roles.length>1) {
					if (!this.rulesForm.role) {
						this.$message.error("请选择角色");
						return;
					}

					let menus = this.menus;
					for (let i = 0; i < menus.length; i++) {
						if (menus[i].roleName == this.rulesForm.role) {
							this.tableName = menus[i].tableName;
						}
					}
				} else {
					this.tableName = this.roles[0].tableName;
					this.rulesForm.role = this.roles[0].roleName;
				}
		
				this.loginPost()
			},
			loginPost() {
				this.$http({
					url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
					method: "post"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.$storage.set("Token", data.token);
						this.$storage.set("role", this.rulesForm.role);
						this.$storage.set("sessionTable", this.tableName);
						this.$storage.set("adminName", this.rulesForm.username);
						this.$nextTick(()=>{
							this.$http({
								url: this.tableName + '/session',
								method: "get"
							}).then(({
								data
							}) => {
								if (data && data.code === 0) {
									if(this.tableName == 'yonghu') {
										this.$storage.set('headportrait',data.data.touxiang)
									}
									if(this.tableName == 'users') {
										this.$storage.set('headportrait',data.data.image)
									}
									this.$storage.set('userForm',JSON.stringify(data.data))
									this.$storage.set('userid',data.data.id);
								} else {
									let message = this.$message
									message.error(data.msg);
								}
								this.$router.replace({ path: "/" });
							});
						})
					} else {
						this.$message.error(data.msg);
					}
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
.login-container {
	min-height: 100vh;
	position: relative;
	background-repeat: no-repeat;
	background-position: center center;
	background-size: cover;
	background-repeat: no-repeat;
	background-size: 50% 100%;
	display: block;
	width: 100%;
	min-height: 100vh;
	justify-content: flex-start;
	align-items: center;
	background-image: url(http://codegen.caihongy.cn/20240929/ec5c51f1ce0845289dd993d890db8d68.png);
	background-position: right top;

	.login-swiper3 {
		margin: 0 auto;
		z-index: 999;
		top: 0;
		left: 0;
		width: 100vw;
		position: fixed;
		height: 100vh;
		.swiper-container {
			.swiper-slide {
				div {
					width: 100%;
					height: 100vh;
					.el-image {
						object-fit: cover;
						width: 100%;
						height: 100vh;
					}
				}
			}
			.swiper-pagination{
				left: 0;
				bottom: 10px;
				width: 100%;
				/deep/ span.swiper-pagination-bullet {
					border-radius: 100%;
					margin: 0 4px;
					background: #000;
					display: inline-block;
					width: 8px;
					opacity: .2;
					height: 8px;
				}
				/deep/ span.swiper-pagination-bullet:hover {
					background: #fff;
					opacity: 1;
				}
				/deep/ span.swiper-pagination-bullet.swiper-pagination-bullet-active {
					background: #fff;
					opacity: 1;
				}
			}
			.swiper-button-next {
				cursor: pointer;
				border-radius: 0;
				margin: -12px 0 0;
				z-index: 9999;
				top: 50%;
				background: none;
				position: absolute;
				.iconfont {
					color: #fff;
					width: 24px;
					font-size: 24px;
					height: 24px;
				}
			}
			.swiper-button-prev {
				cursor: pointer;
				margin: -12px 0 0;
				z-index: 9999;
				top: 50%;
				background: none;
				position: absolute;
				.iconfont {
					color: #fff;
					width: 24px;
					font-size: 24px;
					height: 24px;
				}
			}
			
			.swiper-button-prev:after {
				display:none;
			}
			.swiper-button-next:after {
				display:none;
			}
		}
	}
	.login_form {
		padding: 40px 140px 40px;
		margin: 0;
		z-index: 1000;
		display: flex;
		min-height: 100vh;
		border-radius: 0;
		box-shadow: inset 0px 0px 0px 0px #000;
		flex-direction: column;
		background: #EFF4FF;
		width: 50%;
		justify-content: center;
		align-items: center;
		position: relative;
		height: auto;
		.login_form2 {
			width: 100%;
		}
		.title-container {
			padding: 0 0px;
			margin: 0 0 30px -100px;
			color: #000;
			left: 0;
			background: none;
			font-weight: 600;
			width: calc(100% + 200px);
			font-size: 22px;
			line-height: 40px;
			text-align: center;
		}
		.list-item {
			padding: 0;
			margin: 0 0 40px;
			display: flex;
			width: calc(100% - 0px);
			position: relative;
			align-items: center;
			.lable {
				color: #000;
				width: 120px;
				font-size: 16px;
				line-height: 40px;
				text-align: right;
			}
			input {
				border: 0px solid #efeff7;
				border-radius: 4px;
				padding: 0 10px;
				color: #666;
				width: 100%;
				font-size: 16px;
				height: 60px;
			}
			input:focus {
				border: 0px solid #efeff7;
				padding: 0 10px;
				outline: none;
				color: #000;
				width: 100%;
				font-size: 16px;
				height: 60px;
			}
			.password-box {
				display: flex;
				width: 100%;
				position: relative;
				align-items: center;
				input {
					border: 0px solid #efeff7;
					padding: 0 10px;
					color: #666;
					width: 100%;
					font-size: 16px;
					height: 60px;
				}
				input:focus {
					border: 0px solid #efeff7;
					padding: 0 10px;
					outline: none;
					color: #000;
					width: 100%;
					font-size: 16px;
					height: 60px;
				}
				.iconfont {
					cursor: pointer;
					z-index: 1;
					color: #000;
					top: 0;
					font-size: 16px;
					line-height: 44px;
					position: absolute;
					right: 5px;
				}
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
		}
		.list-type {
			padding: 0;
			margin: 0;
			background: none;
			width: calc(100% - 0px);
			line-height: 60px;
			height: 60px;
			/deep/ .el-radio__input .el-radio__inner {
				background: rgba(53, 53, 53, 0);
				border-color: #666;
			}
			/deep/ .el-radio__input.is-checked .el-radio__inner {
				background: #7EA0F6;
				border-color: #7EA0F6;
			}
			/deep/ .el-radio__label {
				color: #666;
				font-size: 16px;
			}
			/deep/ .el-radio__input.is-checked+.el-radio__label {
				color: #7EA0F6;
				font-size: 16px;
			}
		}
		.login-btn {
			margin: 20px auto;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			flex-wrap: wrap;
			.login-btn1 {
				display: flex;
				width: 100%;
				justify-content: center;
				order: 2;
			}
			.login-btn2 {
				margin: 0 0 30px;
				display: flex;
				width: 70%;
				justify-content: space-around;
				align-items: center;
				flex-wrap: wrap;
				order: 1;
			}
			.login-btn3 {
				width: 100%;
				order: 3;
			}
			.loginInBt {
				border: 0px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				border-radius: 30px;
				padding: 0 10px;
				margin: 0 auto 50px;
				color: #fff;
				background: #7EA0F6;
				font-weight: 600;
				width: 80%;
				font-size: 24px;
				min-width: 68px;
				height: 60px;
			}
			.loginInBt:hover {
				opacity: 0.8;
			}
			.register {
				border: 0px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				border-radius: 5px;
				padding: 0 10px;
				margin: 0 0 10px;
				color: #5D3075;
				background: #fff;
				width: 30%;
				font-size: 16px;
				height: 40px;
			}
			.register:hover {
				opacity: 0.8;
			}
			.forget {
				border: 0;
				cursor: pointer;
				border-radius: 0;
				padding: 0;
				margin: 0 10px 10px 0;
				color: #505050;
				background: none;
				width: 100%;
				font-size: 14px;
				text-align: center;
				height: 34px;
			}
			.forget:hover {
				color: #0d6efd;
				opacity: 1;
			}
		}
	}
}

</style>
