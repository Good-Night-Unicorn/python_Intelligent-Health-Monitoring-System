<template>
	<div>

		<div class="container">
			<el-form class='rgs-form animate__animated animate__' v-if="pageFlag=='register'" ref="registerForm" :model="registerForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">智能健康检测系统设计与实现注册</p></div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="yonghuzhanghao">
						<div class="label" :class="changeRules('yonghuzhanghao')?'required':''">用户账号：</div>
						<el-input v-model="registerForm.yonghuzhanghao"  placeholder="请输入用户账号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="yonghuxingming">
						<div class="label" :class="changeRules('yonghuxingming')?'required':''">用户姓名：</div>
						<el-input v-model="registerForm.yonghuxingming"  placeholder="请输入用户姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="lianxifangshi">
						<div class="label" :class="changeRules('lianxifangshi')?'required':''">联系方式：</div>
						<el-input v-model="registerForm.lianxifangshi"  placeholder="请输入联系方式" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="touxiang">
						<div class="label" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
							@change="yonghutouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="nianling">
						<div class="label" :class="changeRules('nianling')?'required':''">年龄：</div>
						<el-input v-model.number="registerForm.nianling"  placeholder="请输入年龄" />
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="submitForm('registerForm')">注册</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</div>
</template>

<script>
	import 'animate.css';

export default {
    //数据集合
    data() {
		return {
            pageFlag : '',
			tableName: '',
			registerForm: {},
			forgetForm: {},
			rules: {},
			requiredRules: {},
            yonghuxingbieOptions: [],
		}
    },
	mounted() {
		if(this.$route.query.pageFlag=='register'){
			this.tableName = this.$route.query.role;
			if(this.tableName=='yonghu'){
				this.registerForm = {
					yonghuzhanghao: '',
					mima: '',
					mima2: '',
					yonghuxingming: '',
					xingbie: '',
					lianxifangshi: '',
					touxiang: '',
					nianling: '',
				}
			}
			if ('yonghu' == this.tableName) {
				this.rules.yonghuzhanghao = [{ required: true, message: '请输入用户账号', trigger: 'blur' }];
				this.requiredRules.yonghuzhanghao = [{ required: true, message: '请输入用户账号', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.yonghuxingming = [{ required: true, message: '请输入用户姓名', trigger: 'blur' }];
				this.requiredRules.yonghuxingming = [{ required: true, message: '请输入用户姓名', trigger: 'blur' }]
			}
			this.yonghuxingbieOptions = "男,女".split(',');
			if ('yonghu' == this.tableName) {
				this.rules.lianxifangshi = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
			}
			if ('yonghu' == this.tableName) {
				this.rules.nianling = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
			}
		}
	},
    created() {
		this.pageFlag = this.$route.query.pageFlag;
    },
    //方法集合
    methods: {
		changeRules(name){
			if(this.requiredRules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
        // 下二随
		yonghutouxiangUploadChange(fileUrls) {
			this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
		},

		// 多级联动参数


		submitForm(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					var url=this.tableName+"/register";
					if(`yonghu` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					this.$http.post(url, this.registerForm).then(res => {
						if (res.data.code === 0) {
							this.$message({
								message: '注册成功',
								type: 'success',
								duration: 1500,
								onClose: () => {
									this.$router.push('/login');
								}
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
		resetForm(formName) {
			this.$refs[formName].resetFields();
		}
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
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
		.rgs-form {
			background-repeat: no-repeat;
			background-size: cover;
			background: url(http://codegen.caihongy.cn/20241125/bd02eb58253641dc81982546a22c4997.gif);
			display: flex;
			width: 100%;
			min-height: 100vh;
			justify-content: flex-end;
			align-items: center;
			background-position: center center;
			.rgs-form2 {
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
				.title {
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
				.subtitle {
					margin: 0 0 10px 0;
					text-shadow: 4px 4px 2px rgba(64, 158, 255, .5);
					color: rgba(64, 158, 255, 1);
					width: 100%;
					font-size: 20px;
					line-height: 44px;
					text-align: center;
				}
				.list-item {
					border-radius: 8px;
					padding: 0;
					box-shadow:  4px 4px 0px 0px #FBE0E5;
					margin: 0 0 20px;
					background: none;
					display: flex;
					width: 100%;
					align-items: center;
					position: relative;
					flex-wrap: wrap;
					/deep/.el-form-item__content {
						display: flex;
						width: 100%;
						justify-content: space-between;
						.label {
							padding: 0 5px 0 0;
							color: #000;
							left: 10px;
							width: 130px;
							font-size: 16px;
							line-height: 60px ;
							position: absolute !important;
							text-align: left;
						}
						
						.required {
							position: relative;
						}
						.required::after{
							color: red;
							left: -10px;
							position: absolute;
							content: "*";
						}
						.el-input {
							width: 100%;
						}
						.el-input .el-input__inner {
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.el-input .el-input__inner:focus {
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.el-input-number {
							width: 100%;
						}
						.el-input-number .el-input__inner {
							text-align: left;
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.el-input-number .el-input-number__decrease {
							display: none;
						}
						.el-input-number .el-input-number__increase {
							display: none;
						}
						.el-select {
							width: 100%;
						}
						.el-select .el-input__inner {
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.el-select .el-input__inner:focus {
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.el-date-editor {
							width: 100%;
						}
						.el-date-editor .el-input__inner {
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.el-date-editor .el-input__inner:focus {
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.el-upload--picture-card {
							background: transparent;
							border: 0;
							border-radius: 0;
							width: auto;
							height: auto;
							line-height: initial;
							vertical-align: middle;
						}
						.upload .upload-img {
							border: 1px solid #FBE0E5;
							margin: 0 0 0 80px;
							color: #999;
							object-fit: cover;
							width: 110px;
							font-size: 20px;
							line-height: 60px;
							height: 60px;
						}
						.el-upload-list .el-upload-list__item {
							border: 1px solid #FBE0E5;
							margin: 0 0 0 80px;
							color: #999;
							object-fit: cover;
							width: 110px;
							font-size: 20px;
							line-height: 60px;
							height: 60px;
							font-size: 14px;
							line-height: 1.8;
						}
						.el-upload .el-icon-plus {
							border: 1px solid #FBE0E5;
							margin: 0 0 0 80px;
							color: #999;
							object-fit: cover;
							width: 110px;
							font-size: 20px;
							line-height: 60px;
							height: 60px;
						}
						.el-upload__tip {
							margin: 0 0 0 80px;
							color: #838fa1;
							font-size: 15px;
						}
						.emailInput {
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							flex: 1;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.emailInput:focus {
							border: 1px solid #FBE0E5;
							border-radius: 0px;
							padding: 0 120px;
							color: #666;
							background: none;
							flex: 1;
							width: 100%;
							font-size: 16px;
							height: 60px ;
						}
						.el-btn {
							border: 0px solid #e6e6e6;
							cursor: pointer;
							border-radius: 5px;
							padding: 0;
							margin: 0 0 0 10px;
							z-index: 999;
							color: #fff;
							background: linear-gradient( 136deg, #FFB4C2 0%, #8FB0FD 100%);
							width: 120px;
							font-size: 15px;
							height: 60px ;
						}
						.el-btn:hover {
							opacity: 0.5;
						}
						
						.el-input__inner::placeholder {
							color: #123;
							font-size: 16px;
						}
						input::placeholder {
							color: #123;
							font-size: 16px;
						}
						.editor {
							border: 1px solid #FBE0E5;
							background: none;
							width: 100%;
							height: auto;
						}
					}
				}
				.register-btn {
					margin: 50px 0 0 0;
					width: 100%;
				}
				.register-btn1 {
					width: 100%;
				}
				.register-btn2 {
					width: 100%;
				}
				.register_btn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 20px auto 5px;
					color: #fff;
					font-weight: 700;
					display: block;
					font-size: 26px;
					border-radius: 5px;
					outline: none;
					background: linear-gradient( 135deg, #FFB3C1 0%, #8FB0FD 100%);
					width: 100%;
					height: 60px;
				}
				.register_btn:hover {
					opacity: 0.5;
				}
				.has_btn {
					cursor: pointer;
					padding: 20px  0;
					color: #000000;
					display: inline-block;
					text-decoration: none;
					font-size: 14px;
					line-height: 1;
				}
				.has_btn:hover {
					opacity: 0.5;
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
	
	::-webkit-scrollbar {
		display: none;
	}
</style>
