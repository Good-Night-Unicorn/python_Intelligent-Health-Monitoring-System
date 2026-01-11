<template>
	<div class="add-update-preview">
		<el-form
			class="add-update-form"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="80px"
			>
			<el-form-item class="add-item" label="用户名" prop="username">
				<el-input v-model="ruleForm.username" 
					placeholder="用户名" clearable :disabled=" false  ||ro.username"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="密码" prop="password">
				<el-input v-model="ruleForm.password" 
					placeholder="密码" clearable :disabled=" false  ||ro.password"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="角色" prop="role">
				<el-input v-model="ruleForm.role" 
					placeholder="角色" clearable :disabled=" false  ||ro.role"></el-input>
			</el-form-item>

			<el-form-item class="add-btn-item">
				<el-button class="submitBtn"  type="primary" @click="onSubmit">
					<span class="icon iconfont icon-kaitongfuwu"></span>
					<span class="text">提交</span>
				</el-button>
				<el-button class="closeBtn" @click="back()">
					<span class="icon iconfont icon-shanchu1"></span>
					<span class="text">取消</span>
				</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				id: '',
				baseUrl: '',
				ro:{
					username : false,
					password : false,
					role : false,
				},
				type: '',
				userTableName: localStorage.getItem('UserTableName'),
				ruleForm: {
					username: '',
					password: '',
					role: '',
				},


				rules: {
					username: [
						{ required: true, message: '用户名不能为空', trigger: 'blur' },
					],
					password: [
						{ required: true, message: '密码不能为空', trigger: 'blur' },
					],
					role: [
					],
				},
				centerType: false,
			};
		},
		computed: {



		},
		components: {
		},
		created() {
			if(this.$route.query.centerType){
				this.centerType = true
			}
			//this.bg();
			let type = this.$route.query.type ? this.$route.query.type : '';
			this.init(type);
			this.baseUrl = this.$config.baseUrl;
		},
		methods: {
			getMakeZero(s) {
				return s < 10 ? '0' + s : s;
			},
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(type) {
				this.type = type;
				if(type=='cross'){
					var obj = JSON.parse(localStorage.getItem('crossObj'));
					for (var o in obj){
						if(o=='username'){
							this.ruleForm.username = obj[o];
							this.ro.username = true;
							continue;
						}
						if(o=='password'){
							this.ruleForm.password = obj[o];
							this.ro.password = true;
							continue;
						}
						if(o=='role'){
							this.ruleForm.role = obj[o];
							this.ro.role = true;
							continue;
						}
					}
				}else if(type=='edit'){
					this.info()
				}

				if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
					localStorage.removeItem('raffleType')
					setTimeout(() => {
						this.onSubmit()
					}, 300)
				}
			},

			// 多级联动参数
			// 多级联动参数
			info() {
				this.$http.get(`users/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.ruleForm = res.data.data;
					}
				});
			},
			// 提交
			async onSubmit() {
				if(!this.ruleForm.id) {
					delete this.ruleForm.userid
				}
				await this.$refs["ruleForm"].validate(async valid => {
					if(valid) {
						if(this.type=='cross'){
							var statusColumnName = localStorage.getItem('statusColumnName');
							var statusColumnValue = localStorage.getItem('statusColumnValue');
							if(statusColumnName && statusColumnName!='') {
								var obj = JSON.parse(localStorage.getItem('crossObj'));
								if(!statusColumnName.startsWith("[")) {
									for (var o in obj){
										if(o==statusColumnName){
											obj[o] = statusColumnValue;
										}
									}
									var table = localStorage.getItem('crossTable');
									await this.$http.post(table+'/update', obj).then(res => {});
								}
							}
						}


						await this.$http.post(`users/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(async res => {
							if (res.data.code == 0) {
								this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
										
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.$router.go(-1);
			},
		}
	};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.add-update-preview {
		padding: 0 calc((100% - 1200px)/2);
		color: #333;
		background: #fafcff;
		width: 100%;
		font-size: 16px;
		.add-update-form {
			border-radius: 20px;
			padding: 30px  0;
			background: #fff;
			display: flex;
			width: 100%;
			clear: both;
			flex-wrap: wrap;
			.add-item.el-form-item {
				padding: 10px;
				margin: 0 0 10px;
				background: #FFFFFFFF;
				width: 50%;
				/deep/ .el-form-item__label {
					padding: 0 10px 0 0;
					color: #000;
					font-weight: 500;
					width: 80px;
					font-size: 14px;
					line-height: 60px;
					text-align: right;
				}
				/deep/ .el-form-item__content {
					margin-left: 80px;
				}
				.el-input {
					width: 100%;
				}
				.el-input /deep/ .el-input__inner {
					border: 1px solid #e2e3e5;
					border-radius: 10px;
					padding: 0 12px;
					outline: none;
					color: rgba(64, 158, 255, 1);
					width: 400px;
					font-size: 14px;
					height: 60px;
				}
				.el-input /deep/ .el-input__inner[readonly="readonly"] {
					border: 1px solid #e2e3e5;
					border-radius: 10px;
					padding: 0 12px;
					outline: none;
					color: #3d3d3d;
					width: 400px;
					font-size: 14px;
					height: 60px;
				}
				.el-input-number /deep/ .el-input__inner {
					text-align: left;
					border: 1px solid #e2e3e5;
					border-radius: 10px;
					padding: 0 12px;
					outline: none;
					color: rgba(64, 158, 255, 1);
					width: 400px;
					font-size: 14px;
					height: 60px;
				}
				.el-input-number /deep/ .is-disabled .el-input__inner {
					text-align: left;
					border: 1px solid #e2e3e5;
					border-radius: 10px;
					padding: 0 12px;
					outline: none;
					color: #3d3d3d;
					width: 400px;
					font-size: 14px;
					height: 60px;
				}
				.el-input-number /deep/ .el-input-number__decrease {
					display: none;
				}
				.el-input-number /deep/ .el-input-number__increase {
					display: none;
				}
				.el-select {
					width: 100%;
				}
				.el-select /deep/ .el-input__inner {
					border: 1px solid #e2e3e5;
					border-radius: 10px;
					padding: 0 12px;
					outline: none;
					color: rgba(64, 158, 255, 1);
					width: 400px;
					font-size: 14px;
					height: 60px;
				}
				.el-select /deep/ .is-disabled .el-input__inner {
					border: 1px solid #e2e3e5;
					border-radius: 10px;
					padding: 0 12px;
					outline: none;
					color: #3d3d3d;
					width: 400px;
					font-size: 14px;
					height: 60px;
				}
				.el-date-editor {
					width: 100%;
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 1px solid #e2e3e5;
					border-radius: 10px;
					padding: 0 30px;
					outline: none;
					color: rgba(64, 158, 255, 1);
					width: 400px;
					font-size: 14px;
					height: 60px;
				}
				.el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
					border: 1px solid #e2e3e5;
					border-radius: 10px;
					padding: 0 30px;
					outline: none;
					color: #3d3d3d;
					width: 400px;
					font-size: 14px;
					height: 60px;
				}
				/deep/ .el-upload--picture-card {
					background: transparent;
					border: 0;
					border-radius: 0;
					width: auto;
					height: auto;
					line-height: initial;
					vertical-align: middle;
				}
				/deep/ .upload .upload-img {
					border: 1px solid #e2e3e5;
					cursor: pointer;
					border-radius: 6px;
					color: #e2e3e5;
					width: 200px;
					font-size: 32px;
					line-height: 200px;
					text-align: center;
					height: 200px;
				}
				/deep/ .el-upload-list .el-upload-list__item {
					border: 1px solid #e2e3e5;
					cursor: pointer;
					border-radius: 6px;
					color: #e2e3e5;
					width: 200px;
					font-size: 32px;
					line-height: 200px;
					text-align: center;
					height: 200px;
					font-size: 14px;
					line-height: 1.8;
				}
				/deep/ .el-upload .el-icon-plus {
					border: 1px solid #e2e3e5;
					cursor: pointer;
					border-radius: 6px;
					color: #e2e3e5;
					width: 200px;
					font-size: 32px;
					line-height: 200px;
					text-align: center;
					height: 200px;
				}
				/deep/ .el-upload__tip {
					color: #838fa1;
				}
				.el-textarea /deep/ .el-textarea__inner {
					border: 1px solid #e2e3e5;
					border-radius: 4px;
					padding: 12px;
					outline: none;
					color: rgba(64, 158, 255, 1);
					width: 400px;
					font-size: 14px;
					height: 120px;
				}
				.el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
					border: 1px solid #e2e3e5;
					border-radius: 4px;
					padding: 12px;
					outline: none;
					color: #3d3d3d;
					width: 400px;
					font-size: 14px;
					height: 120px;
				}
				/deep/ .el-input__inner::placeholder {
					color: #123;
					font-size: 16px;
				}
				/deep/ textarea::placeholder {
					color: #123;
					font-size: 16px;
				}
				.editor {
					border: 1px solid #e2e3e5;
					background-color: #fff;
					border-radius: 0;
					padding: 0;
					margin: 0;
					width: 100%;
					border-color: #ccc;
					border-width: 0;
					border-style: solid;
					height: auto;
				}
				.upload-img {
					width: 150px;
					height: 150px;
				}
				.viewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 40px;
					border-radius: 4px;
					outline: none;
					background: linear-gradient( 134deg, #90B0FD 0%, #FFB4C2 100%);
					width: auto;
					height: 40px;
				}
				.viewBtn:hover {
					color: #666;
					background: rgba(64, 158, 255, .5);
				}
				.unviewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 40px;
					border-radius: 4px;
					outline: none;
					background: #FFBDC5D6;
					width: auto;
					height: 40px;
				}
				.unviewBtn:hover {
					color: #666;
					background: rgba(85, 85, 127, .5);
				}
			}
			.add-btn-item {
				padding: 0;
				margin: 0;
				.submitBtn {
					border: 0;
					cursor: pointer;
					border-radius: 0;
					padding: 0 15px;
					margin: 0 20px 0 0;
					outline: none;
					background: linear-gradient( 134deg, #90B0FD 0%, #FFB4C2 100%);
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
					.icon {
						color: rgba(255, 255, 255, 1);
					}
					.text {
						color: rgba(255, 255, 255, 1);
					}
				}
				.submitBtn:hover {
					background: rgba(64, 158, 255, .5);
					.icon {
						color: #000;
					}
					.text {
						color: #000;
					}
				}
				.closeBtn {
					border: 0;
					cursor: pointer;
					padding: 0 15px;
					margin: 0 20px 0 0;
					color: #FFFFFFFF;
					display: inline-block;
					font-size: 14px;
					line-height: 40px;
					border-radius: 0;
					outline: none;
					background: #bdc5d6;
					width: auto;
					height: 40px;
					.icon {
						color: #FFFFFFFF;
					}
					.text {
						color: #FFFFFFFF;
					}
				}
				.closeBtn:hover {
					color: rgba(64, 158, 255, .5);
					border-color: rgba(64, 158, 255, .5);
					.icon {
						color: rgba(64, 158, 255, 0.5);
					}
					.text {
						color: #FFFFFFFF;
					}
				}
			}
		}
	}
	.el-date-editor.el-input {
		width: auto;
	}
</style>
