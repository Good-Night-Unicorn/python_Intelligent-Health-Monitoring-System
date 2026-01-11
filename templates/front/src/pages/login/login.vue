<template>
	<div>
		<div class="login-container">
			<el-form ref="loginForm" :model="loginForm" :rules="rules" class="login_form animate__animated animate__">
				<div class="login_form2">
					<div class="login-title">智能健康检测系统设计与实现登录</div>
					<div v-if="loginType==1" class="list-item" prop="username">
						<div class="lable">
							账号：
						</div>
						<input v-model="loginForm.username" placeholder="请输入账号：">
					</div>
					<div v-if="loginType==1" class="list-item" prop="password">
						<div class="lable">
							密码：
						</div>
						<div class="password-box">
							<input v-model="loginForm.password" placeholder="请输入密码：" :type="showPassword?'text':'password'">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item" v-if="roles.length>1">
						<div class="lable">
							
						</div>
						<div class="list-type" prop="role">
							<el-radio v-model="loginForm.tableName" :label="item.tableName" v-for="(item, index) in roles" :key="index" @change.native="getCurrentRow(item)">{{item.roleName}}</el-radio>
						</div>
					</div>

			
					<div class="list-btn">
						<el-button class="login_btn" v-if="loginType==1" @click="submitForm('loginForm')">登录</el-button>

						<div class="list-btn2">
							<router-link class="register_btn" :to="{path: '/register', query: {role: item.tableName,pageFlag:'register'}}" v-if="item.hasFrontRegister=='是'" v-for="(item, index) in roles2" :key="index">注册{{item.roleName.replace('注册','')}}</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</template>

<script>
	import 'animate.css';
import menu from '@/config/menu'
export default {
	//数据集合
	data() {
		return {
            baseUrl: this.$config.baseUrl,
            loginType: 1,
			roleMenus: [],
			loginForm: {
				username: '',
				password: '',
				tableName: '',
			},
			role: '',
			roles: [],
			roles2: [],
			rules: {
				username: [
					{ required: true, message: '请输入账号', trigger: 'blur' }
				],
				password: [
					{ required: true, message: '请输入密码', trigger: 'blur' }
				]
			},
			codes: [{
				num: 1,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 2,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 3,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 4,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}],
			flag: false,
			verifyCheck2: false,
			showPassword: false,
		}
	},
	components: {
	},
	created() {
		this.roleMenus = menu.list()
		for(let item in this.roleMenus) {
			if(this.roleMenus[item].hasFrontLogin=='是') {
				this.roles.push(this.roleMenus[item]);
			}
			if(this.roleMenus[item].hasFrontRegister=='是') {
				this.roles2.push(this.roleMenus[item]);
			}
		}
		
	},
	mounted() {
	},
	//方法集合
	methods: {
		randomString() {
			var len = 4;
			var chars = [
				'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
				'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
				'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
				'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
				'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
				'3', '4', '5', '6', '7', '8', '9'
			]
			var colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
			var sizes = ['14', '15', '16', '17', '18']
			
			var output = []
			for (var i = 0; i < len; i++) {
				// 随机验证码
				var key = Math.floor(Math.random() * chars.length)
				this.codes[i].num = chars[key]
				// 随机验证码颜色
				var code = '#'
				for (var j = 0; j < 6; j++) {
					var key = Math.floor(Math.random() * colors.length)
					code += colors[key]
				}
				this.codes[i].color = code
				// 随机验证码方向
				var rotate = Math.floor(Math.random() * 45)
				var plus = Math.floor(Math.random() * 2)
				if (plus == 1) rotate = '-' + rotate
				this.codes[i].rotate = 'rotate(' + rotate + 'deg)'
				// 随机验证码字体大小
				var size = Math.floor(Math.random() * sizes.length)
				this.codes[i].size = sizes[size] + 'px'
			}
		},
		getCurrentRow(row) {
			this.role = row.roleName;
		},
		submitForm(formName) {
			if (this.roles.length!=1) {
				if (!this.role) {
					this.$message.error("请选择登录用户类型");
					return false;
				}
			} else {
				this.role = this.roles[0].roleName;
				this.loginForm.tableName = this.roles[0].tableName;
			}
			if (!this.loginForm.username) {
				this.$message.error("请输入用户名");
				return;
			}
			if (!this.loginForm.password) {
				this.$message.error("请输入密码");
				return;
			}

			this.loginPost(formName)
		},
		loginPost(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					this.$http.get(`${this.loginForm.tableName}/login`, {params: this.loginForm}).then(res => {
						if (res.data.code === 0) {
							localStorage.setItem('frontToken', res.data.token);
							localStorage.setItem('UserTableName', this.loginForm.tableName);
							localStorage.setItem('username', this.loginForm.username);
							localStorage.setItem('frontSessionTable', this.loginForm.tableName);
							localStorage.setItem('frontRole', this.role);
							localStorage.setItem('keyPath', 0);
							this.$router.push('/');
							this.$message({
								message: '登录成功',
								type: 'success',
								duration: 1500,
							});
						} else {
							this.$message.error(res.data.msg);
						}
					});
				} else {
					return false;
				}
			});
		},
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.login-container {
		background-repeat: no-repeat;
		background-size: cover;
		background: url(http://codegen.caihongy.cn/20241125/bd02eb58253641dc81982546a22c4997.gif);
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: flex-end;
		align-items: center;
		background-position: center center;
		position: relative;
		background: url(http://codegen.caihongy.cn/20241125/bd02eb58253641dc81982546a22c4997.gif);
		.login_form {
			border-radius: 10px;
			padding: 91px 80px 91px 50px;
			margin: 0;
			z-index: 1;
			background: #fbfbfb;
			width: 780px;
			min-height: 100vh;
			border-color: #FBE0E5;
			border-width: 0 0 0 15px;
			border-style: solid;
			height: auto;
			.login_form2 {
				width: 100%;
				.login-title {
					margin: 0 0 40px 0;
					color: #C998A4;
					white-space: nowrap;
					font-weight: 600;
					font-size: 18px;
					border-color: #FFB4C2;
					line-height: 90px;
					border-radius: 5px;
					background: #fff;
					width: 100%;
					border-width: 10px 0 0 0;
					border-style: solid;
					text-align: center;
					height: 90px;
				}
				.list-item {
					padding: 0;
					box-shadow: 4px 4px 0px 0px #FBE0E5;
					margin: 15px 0 15px 10px;
					background: none;
					display: flex;
					width: 100%;
					align-items: center;
					position: relative;
					height: 60px;
					.lable {
						border: 0 ;
						z-index: 2;
						color: #333333;
						left: 10px;
						letter-spacing: 1px;
						width: auto;
						font-size: 16px;
						line-height: 60px;
						position: absolute;
						text-align: left;
						min-width: 60px;
						height: 60px;
					}
					input {
						border: 1px solid #FBE0E5;
						padding: 0 72px;
						color: #666;
						flex: 1;
						background: none;
						width: 100%;
						font-size: 16px;
						line-height: 60px;
						position: absolute;
						height: 60px;
					}
					input:focus {
						border: 1px solid #FBE0E5;
						padding: 0 72px;
						outline: none;
						color: #666;
						flex: 1;
						background: none;
						width: 100%;
						font-size: 16px;
						line-height: 60px;
						height: 60px;
					}
					.password-box {
						margin: 15px 0;
						display: flex;
						width: 100%;
						align-items: center;
						input {
							border: 1px solid #FBE0E5;
							padding: 0 72px;
							outline: none;
							color: #666;
							flex: 1;
							background: none;
							width: 100%;
							font-size: 16px;
							line-height: 60px;
							height: 60px;
						}
						input:focus {
							border: 1px solid #FBE0E5;
							padding: 0 72px;
							outline: none;
							color: #666;
							flex: 1;
							background: none;
							width: 100%;
							font-size: 16px;
							line-height: 60px;
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
						color: #123;
						font-size: 16px;
					}
				}
				.list-type {
					margin: 20px auto;
					display: flex;
					width: 80%;
					align-items: center;
					/deep/ .el-radio__input .el-radio__inner {
						background: #FFB4C2;
						border-color: #666666;
					}
					/deep/ .el-radio__input.is-checked .el-radio__inner {
						background: #8FB0FD;
						border-color: #8FB0FD;
					}
					/deep/ .el-radio__label {
						color: #FFB4C2;
						font-size: 14px;
					}
					/deep/ .el-radio__input.is-checked+.el-radio__label {
						color: #8FB0FD;
						font-size: 14px;
					}
				}
				.list-btn {
					margin: 50px 0 50px 10px;
					width: 100%;
					.login_btn {
						border: 0;
						cursor: pointer;
						border-radius: 4px;
						padding: 0 24px;
						margin: 0;
						outline: none;
						color: #fff;
						background: linear-gradient( 135deg, #FFB3C1 0%, #8FB0FD 100%);
						font-weight: 700;
						width: 100%;
						font-size: 26px;
						height: 60px;
					}
					.login_btn:hover {
						opacity: 0.5;
					}
					.list-btn2 {
						margin: 50px 0;
						display: flex;
						width: 100%;
						flex-wrap: wrap;
						.register_btn {
							cursor: pointer;
							border: 2px solid ;
							margin: 0  0 25px 0;
							color: #000000;
							background: #fff;
							border-image:  linear-gradient(135deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 2 2;
							text-decoration: none;
							width: 100%;
							font-size: 14px;
							line-height: 60px;
							text-align: center;
							height: 60px;
						}
						.register_btn:hover {
							opacity: 0.5;
						}
						.resetpwd_btn {
							cursor: pointer;
							border: 2px solid ;
							margin: 0  0 25px 0;
							color: #000000;
							background: #fff;
							border-image:  linear-gradient(135deg, rgba(255, 180.00000447034836, 194.00000363588333, 1), rgba(143.00000667572021, 176.00000470876694, 253.0000001192093, 1)) 2 2;
							text-decoration: none;
							width: 100%;
							font-size: 14px;
							line-height: 60px;
							text-align: center;
							height: 60px;
						}
						.resetpwd_btn:hover {
							opacity: 0.5;
						}
					}
				}
			}
			.idea1 {
				background: red;
				display: none;
				width: 100%;
				height: 40px;
			}
			.idea2 {
				background: blue;
				display: none;
				width: 100%;
				height: 40px;
			}
		}
	}
</style>
