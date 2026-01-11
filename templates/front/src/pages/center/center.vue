<template>
	<div class="center-preview">
		<div class="center-title">{{ title }}</div>
		<div class="center-info">
			<div class="center-info-title">个人信息</div>

			<div class="img-box" v-if="userTableName=='yonghu'">
				<img :src="sessionForm.touxiang?baseUrl + sessionForm.touxiang:require('@/assets/avator.png')">
			</div>
			<div class="info-item1" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">用户账号：</div>
				<div class="text">{{sessionForm.yonghuzhanghao}}</div>
			</div>
			<div class="info-item2" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">用户姓名：</div>
				<div class="text">{{sessionForm.yonghuxingming}}</div>
			</div>
			<div class="info-item3" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">性别：</div>
				<div class="text">{{sessionForm.xingbie}}</div>
			</div>
			<div class="info-item4" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">联系方式：</div>
				<div class="text">{{sessionForm.lianxifangshi}}</div>
			</div>
			<div class="info-item5" v-if="userTableName=='yonghu'">
				<span class="icon iconfont icon-shouye-zhihui"></span>
				<div class="label">年龄：</div>
				<div class="text">{{sessionForm.nianling}}</div>
			</div>
		
		</div>
	
		<el-tabs class="center-tabs" tab-position="left" @tab-click="handleClick">
			<el-tab-pane label="个人中心">
				<el-form class="center-preview-pv" ref="sessionForm" :model="sessionForm" :rules="rules" label-width="150px">
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="用户账号" prop="yonghuzhanghao">
						<el-input v-model="sessionForm.yonghuzhanghao" placeholder="用户账号" readonly></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="用户姓名" prop="yonghuxingming">
						<el-input v-model="sessionForm.yonghuxingming" placeholder="用户姓名" ></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="性别" prop="xingbie">
						<el-select v-model="sessionForm.xingbie" placeholder="请选择性别" >
							<el-option v-for="(item, index) in dynamicProp.xingbie" :key="index" :label="item" :value="item"></el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="联系方式" prop="lianxifangshi">
						<el-input v-model="sessionForm.lianxifangshi" placeholder="联系方式" ></el-input>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="头像" prop="touxiang">
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="sessionForm.touxiang?sessionForm.touxiang:''"
							@change="yonghutouxiangHandleAvatarSuccess"
							></file-upload>
					</el-form-item>
					<el-form-item class="center-item" v-if="userTableName=='yonghu'" label="年龄" prop="nianling">
						<el-input v-model="sessionForm.nianling" placeholder="年龄" ></el-input>
					</el-form-item>
					<el-form-item class="center-btn-item">
						<div class="updateBtn" type="primary" @click="onSubmit('sessionForm')">
							<span class="icon iconfont icon-kaitongfuwu"></span>
							<span class="text">更新信息</span>
						</div>
						<div class="closeBtn" type="danger" @click="logout">
							<span class="icon iconfont icon-shanchu1"></span>
							<span class="text">退出登录</span>
						</div>
					</el-form-item>
				</el-form>
			</el-tab-pane>
			<el-tab-pane label="修改密码">
				<el-form class="center-preview-pv" ref="passwordForm" :model="passwordForm" :rules="passwordRules" label-width="150px">
					<el-form-item class="center-item" label="原密码" prop="password">
						<el-input type="password" v-model="passwordForm.password" placeholder="原密码"></el-input>
					</el-form-item>
					<el-form-item class="center-item" label="新密码" prop="newpassword">
						<el-input type="password" v-model="passwordForm.newpassword" placeholder="新密码"></el-input>
					</el-form-item>
					<el-form-item class="center-item" label="确认密码" prop="repassword">
						<el-input type="password" v-model="passwordForm.repassword" placeholder="确认密码"></el-input>
					</el-form-item>
					<el-form-item class="center-btn-item">
						<div class="updateBtn" type="primary" @click="updatePassword">
							<span class="icon iconfont icon-kaitongfuwu"></span>
							<span class="text">修改密码</span>
						</div>
					</el-form-item>
				</el-form>
			</el-tab-pane>
			<el-tab-pane v-for="(item,index) in menuList" :key="index" v-if="hasBack(item.menu)" :label="item.child[0].menu" :name="item.child[0].tableName"></el-tab-pane>
			<el-tab-pane label="我的收藏"></el-tab-pane>
		</el-tabs>

	</div>
</template>

<script>
	import config from '@/config/config';
	import menu from '@/config/menu';
	import Vue from 'vue';
	export default {
		//数据集合
		data() {
			return {
				title: '个人中心',
				baseUrl: config.baseUrl,
				sessionForm: {},
				passwordForm: {},
				passwordRules: {
					password: [
						{
							required: true,
							message: "密码不能为空",
							trigger: "blur"
						}
					],
					newpassword: [
						{
							required: true,
							message: "新密码不能为空",
							trigger: "blur"
						}
					],
					repassword: [
						{
							required: true,
							message: "确认密码不能为空",
							trigger: "blur"
						}
					]
				},
				rules: {},
				menuList: [],
				disabled: false,
				uploadUrl: config.baseUrl + 'file/upload',
				imageUrl: '',
				headers: {Token: localStorage.getItem('frontToken')},
				userTableName: localStorage.getItem('UserTableName'),
				dynamicProp: {},
			}
		},
		created() {
			let menus = menu.list()
			for(let x in menus){
				if(menus[x].tableName == this.userTableName){
					for(let i in menus[x].backMenu){
						if(menus[x].backMenu[i].menu=='考试管理'){
							menus[x].backMenu.splice(i,1)
						}
					}
					this.menuList = menus[x].backMenu
				}
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'yonghuzhanghao', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'mima', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'yonghuxingming', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'xingbie', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'lianxifangshi', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'touxiang', null);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.sessionForm, 'nianling', null);
			}

			if ('yonghu' == this.userTableName&&this.rules['yonghuzhanghao']){
				this.rules['yonghuzhanghao'].push({ required: true, message: '请输入用户账号', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['yonghuzhanghao']) {
				this.$set(this.rules, 'yonghuzhanghao', [{ required: true, message: '请输入用户账号', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName&&this.rules['mima']){
				this.rules['mima'].push({ required: true, message: '请输入密码', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['mima']) {
				this.$set(this.rules, 'mima', [{ required: true, message: '请输入密码', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName&&this.rules['yonghuxingming']){
				this.rules['yonghuxingming'].push({ required: true, message: '请输入用户姓名', trigger: 'blur' })
			}else if('yonghu' == this.userTableName&&!this.rules['yonghuxingming']) {
				this.$set(this.rules, 'yonghuxingming', [{ required: true, message: '请输入用户姓名', trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.rules, 'lianxifangshi', [{ required: false, validator: this.$validate.isMobile, trigger: 'blur' }]);
			}
			if ('yonghu' == this.userTableName) {
				this.$set(this.rules, 'nianling', [{ required: false, validator: this.$validate.isIntNumer, trigger: 'blur' }]);
			}

			this.init();
			this.sessionForm = JSON.parse(localStorage.getItem('sessionForm'))
		},
		//方法集合
		methods: {
			init() {
				if ('yonghu' == this.userTableName) {
					this.dynamicProp.xingbie = '男,女'.split(',');
				}
			},
			setSession(){
				localStorage.setItem('sessionForm',JSON.stringify(this.sessionForm))
			},
			onSubmit(formName) {
				if(`yonghu` == this.userTableName && this.sessionForm.touxiang!=null){
					this.sessionForm.touxiang = this.sessionForm.touxiang.replace(new RegExp(this.$config.baseUrl,"g"),"");
				}
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.$http.post(this.userTableName + '/update', this.sessionForm).then(res => {
							if (res.data.code == 0) {
								this.setSession()
								this.$message({
									message: '更新成功',
									type: 'success',
									duration: 1500
								});
							}
						});
					} else {
						return false;
					}
				});
			},
			yonghutouxiangHandleAvatarSuccess(fileUrls) {
				this.sessionForm.touxiang = fileUrls;
			},
			handleClick(tab, event) {
				switch(event.target.outerText) {
					case '个人中心':
						tab.$router.push('/index/center');
						break;
					case '修改密码':
						this.passwordForm = {
							password: '',
							newpassword: '',
							repassword: '',
						}
						this.$forceUpdate()
						break;
					case '我的收藏':
						localStorage.setItem('storeupType', 1);
						tab.$router.push('/index/storeup');
						break;
					default:
						tab.$router.push(`/index/${tab.name}?centerType=1`);
				}

				this.title = event.target.outerText;
			},
			async updatePassword(){
				this.$refs["passwordForm"].validate(async valid => {
					if (valid) {
						var password = "";
						if (this.sessionForm.mima) {
							password = this.sessionForm.mima;
						} else if (this.sessionForm.password) {
							password = this.sessionForm.password;
						}
						if (this.userTableName == 'yonghu') {
						}
						if (this.passwordForm.password != password) {
							this.$message.error("原密码错误");
							return;
						}
						if (this.passwordForm.newpassword != this.passwordForm.repassword) {
							this.$message.error("两次密码输入不一致");
							return;
						}
						if (this.passwordForm.newpassword == this.passwordForm.password) {
							this.$message.error("新密码与原密码相同！");
							return;
						}
						this.sessionForm.password = this.passwordForm.newpassword;
						this.sessionForm.mima = this.passwordForm.newpassword;
						this.$http.post(`${this.userTableName}/update`,this.sessionForm).then(({data})=>{
							if (data && data.code === 0) {
								this.$message({
									message: "修改密码成功,下次登录系统生效",
									type: "success",
									duration: 1500,
									onClose: () => {
									}
								});
								this.setSession()
							} else {
								this.$message.error(data.msg);
							}
						});
					}
				})
			},
			logout() {
				localStorage.clear();
				Vue.http.headers.common['Token'] = "";
				this.$router.push('/index/home');
				this.activeIndex = '0'
				localStorage.setItem('keyPath', this.activeIndex)
				this.$forceUpdate()
				this.$message({
					message: '登出成功',
					type: 'success',
					duration: 1500,
				});
			},
			hasBack(name){
				switch(name){
					case '我的收藏管理':
						return false
						break;
					default:
						return true
				}
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.center-preview {
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
		.center-title {
			padding: 0 0 50px 0;
			margin: 10px auto;
			color: #000;
			background: url(http://codegen.caihongy.cn/20241205/b08c6150728242b18bc30581dde4b827.png) no-repeat bottom center /   100%;
			font-weight: 700;
			width: 101%;
			font-size: 30px;
			line-height: 54px;
			text-align: center;
		}
		.center-info {
			padding: 20px;
			margin: 30px 0 0 30px;
			color: #fff;
			display: flex;
			font-size: 16px;
			border-color: #F2EEE9;
			float: right;
			flex-wrap: wrap;
			background: #fff;
			width: 350px;
			border-width: 0;
			position: relative;
			border-style: solid;
			order: 2;
			.center-info-title {
				color: red;
				background: radial-gradient(circle, rgba(237,94,91,1) 0%, rgba(209,6,2,1) 100%);
				display: none;
				width: 100%;
				font-size: 16px;
				line-height: 50px;
				text-align: center;
				height: 50px;
			}
			.img-box {
				margin: 0 0 20px 0 ;
				width: 100%;
				font-size: 0;
				border-color: #efefef;
				border-width: 0;
				border-style: solid;
				height: auto;
				img {
					border-radius: 100%;
					margin: 0 auto;
					object-fit: cover;
					display: block;
					width: 80px;
					border-color: #efefef;
					border-width: 0 0 1px 0;
					border-style: solid;
					height: 80px;
				}
			}
			.info-item1 {
				border: 1px solid;
				border-radius: 10px;
				padding: 15px 20px;
				margin: 0 0 20px 0;
				color: #000;
				display: flex;
				width: 100%;
				border-color: #eda7b4;
				align-items: center;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #000;
					font-size: 14px;
				}
				.label {
					margin: 0 15px 0 0;
					color: #000;
					font-size: 14px;
				}
				.text {
					color: #000;
					flex: 1;
					font-size: 14px;
					text-align: left;
				}
			}
			.info-item2 {
				border: 1px solid;
				border-radius: 10px;
				padding: 15px 20px;
				margin: 0 0 20px 0;
				color: #000;
				display: flex;
				width: 100%;
				border-color: #eda7b4;
				align-items: center;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #333;
					font-size: 14px;
				}
				.label {
					margin: 0 15px 0 0;
					color: #333;
					font-size: 14px;
				}
				.text {
					color: #333;
					flex: 1;
					font-size: 14px;
				}
			}
			.info-item3 {
				border: 1px solid;
				border-radius: 10px;
				padding: 15px 20px;
				margin: 0 0 20px 0;
				color: #000;
				display: flex;
				width: 100%;
				border-color: #eda7b4;
				align-items: center;
				flex-wrap: wrap;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #333;
					font-size: 14px;
				}
				.label {
					margin: 0 15px 0 0;
					color: #333;
					font-size: 14px;
				}
				.text {
					color: #333;
					flex: 1;
					font-size: 14px;
				}
			}
			.info-item4 {
				border: 1px solid;
				border-radius: 10px;
				padding: 10px 20px;
				margin: 0 0 20px 0;
				color: #000;
				display: flex;
				width: 100%;
				border-color: #eda7b4;
				align-items: center;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #333;
					font-size: 14px;
				}
				.label {
					margin: 0 15px 0 0;
					color: #333;
					font-size: 14px;
				}
				.text {
					color: #333;
					flex: 1;
					font-size: 14px;
				}
			}
			.info-item5 {
				border: 1px solid;
				border-radius: 10px;
				padding: 10px 20px;
				margin: 0 0 20px 0;
				color: #000;
				display: flex;
				width: 100%;
				border-color: #eda7b4;
				align-items: center;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #333;
					font-size: 14px;
				}
				.label {
					margin: 0 15px 0 0;
					color: #333;
					font-size: 14px;
				}
				.text {
					color: #333;
					flex: 1;
					font-size: 14px;
				}
			}
			.info-item6 {
				border: 1px solid;
				border-radius: 10px;
				padding: 10px 20px;
				margin: 0 0 20px 0;
				color: #000;
				display: flex;
				width: 100%;
				border-color: #eda7b4;
				align-items: center;
				height: auto;
				.icon {
					padding: 0 5px;
					color: #333;
					font-size: 14px;
				}
				.label {
					margin: 0 15px 0 0;
					color: #333;
					font-size: 14px;
				}
				.text {
					color: #333;
					flex: 1;
					font-size: 14px;
				}
			}
		}
		.center-tabs.el-tabs {
			border-radius: 20px;
			margin: 40px 0px 0 0;
			background: none;
			flex: 1;
			width: calc(100% - 380px);
			height: auto;
			order: 1;
			/deep/ .el-tabs__header {
				padding: 0 20px;
				background: #fff;
				width: 100%;
				border-color: #9e9e9e;
				border-width: 0 0 1px 0;
				position: relative;
				border-style: solid;
				text-align: center;
				height: auto;
			}
			/deep/ .el-tabs__header .el-tabs__item {
				border: 0;
				padding: 0 10px;
				margin: 0 10px;
				color: #9e9e9e;
				font-weight: 500;
				display: block;
				font-size: inherit;
				line-height: 60px;
				float: left;
				border-radius: 0px;
				background: none;
				position: relative;
				text-align: center;
				height: 60px;
			}
			/deep/ .el-tabs__header .el-tabs__item:hover {
				color: #90b0fd;
				display: block;
				border-color: #ffb4c2;
				border-width: 0 0 2px 0;
				border-style: solid;
			}
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				color: #90b0fd;
				display: block;
				font-size: 16px;
				border-color: #ffb4c2;
				border-width: 0 0 2px 0;
				line-height: 60px;
				float: left;
				border-style: solid;
				height: 60px;
			}
			/deep/ .el-tabs__content {
				padding: 30px 0;
				background: #fff;
				width: 100%;
			}
			/deep/ .el-tabs__content .el-tab-pane {
				width: 100%;
			}
			& /deep/ .el-tabs__header {
				.el-tabs__nav{
					overflow: auto;
				}
				::-webkit-scrollbar {
					-webkit-appearance: none;
					width: 6px;
					height: 6px;
				}
				::-webkit-scrollbar-track {
					background: rgba(0, 0, 0, 0.1);
					border-radius: 0;
				}
				::-webkit-scrollbar-thumb {
					cursor: pointer;
					border-radius: 5px;
					background: rgba(0, 0, 0, 0.15);
					transition: color 0.2s ease;
				}
				::-webkit-scrollbar-thumb:hover {
					background: rgba(0, 0, 0, 0.3);
				}
				.el-tabs__nav-wrap {
					margin: 0;
					&::after {
						content: none;
					}
				}
				.el-tabs__active-bar {
					display: none !important;
				}
			}
			.center-preview-pv {
				.center-item.el-form-item {
					padding: 10px 100px 10px 10px;
					margin: 0 0 10px;
					background: #fff;
					width: 100%;
					/deep/ .el-form-item__label {
						padding: 0 10px 0 0;
						color: #000;
						font-weight: 500;
						width: 150px;
						font-size: 14px;
						line-height: 40px;
						text-align: right;
					}
					.el-form-item__content {
						margin-left: 150px;
					}
					.el-input {
						width: 100%;
					}
					.el-input /deep/ .el-input__inner {
						border: 1px solid #e2e3e5;
						border-radius: 10px;
						padding: 0 12px;
						outline: none;
						color: #666;
						width: 100%;
						font-size: 15px;
						height: 60px;
					}
					.el-input /deep/ .el-input__inner[readonly="readonly"] {
						border: 1px solid #e2e3e5;
						border-radius: 10px;
						padding: 0 12px;
						outline: none;
						color: #666;
						width: 100%;
						font-size: 15px;
						height: 60px;
					}
					.el-select {
						width: 100%;
					}
					.el-select /deep/ .el-input__inner {
						border: 1px solid #e2e3e5;
						border-radius: 10px;
						padding: 0 12px;
						outline: none;
						color: #666;
						width: 100%;
						font-size: 15px;
						height: 60px;
					}
					.el-select /deep/ .is-disabled .el-input__inner {
						border: 1px solid #e2e3e5;
						border-radius: 10px;
						padding: 0 12px;
						outline: none;
						color: #666;
						width: 100%;
						font-size: 15px;
						height: 60px;
					}
					.el-date-editor {
						width: 100%;
					}
					.el-date-editor /deep/ .el-input__inner {
						border: 1px solid #e2e3e5;
						border-radius: 10px;
						padding: 0 32px;
						outline: none;
						color: #666;
						width: 100%;
						font-size: 15px;
						height: 60px;
					}
					.el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
						border: 1px solid #e2e3e5;
						border-radius: 10px;
						padding: 0 32px;
						outline: none;
						color: #666;
						width: 100%;
						font-size: 15px;
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
						color: #888;
						width: 120px;
						font-size: 32px;
						line-height: 60px;
						text-align: center;
						height: 60px;
					}
					/deep/ .el-upload-list .el-upload-list__item {
						border: 1px solid #e2e3e5;
						cursor: pointer;
						border-radius: 6px;
						color: #888;
						width: 120px;
						font-size: 32px;
						line-height: 60px;
						text-align: center;
						height: 60px;
						font-size: 14px;
						line-height: 1.8;
					}
					/deep/ .el-upload .el-icon-plus {
						border: 1px solid #e2e3e5;
						cursor: pointer;
						border-radius: 6px;
						color: #888;
						width: 120px;
						font-size: 32px;
						line-height: 60px;
						text-align: center;
						height: 60px;
					}
					/deep/ .el-upload__tip {
						color: #838fa1;
						font-size: 15px;
					}
					/deep/ .el-input__inner::placeholder {
						color: #123;
						font-size: 16px;
					}
				}
				.center-btn-item {
					padding: 0;
					margin: 0;
					.updateBtn {
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
					.updateBtn:hover {
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
						color: #FFF;
						display: inline-block;
						font-size: 14px;
						line-height: 40px;
						border-radius: 0;
						outline: none;
						background: #bdc5d6;
						width: auto;
						height: 40px;
						.icon {
							color: #FFF;
						}
						.text {
							color: #FFF;
						}
					}
					.closeBtn:hover {
						color: rgba(64, 158, 255, .5);
						border-color: rgba(64, 158, 255, .5);
						.icon {
							color: rgba(64, 158, 255, 0.5);
						}
						.text {
							color: rgba(64, 158, 255, 0.5);
						}
					}
				}
				.el-date-editor.el-input {
					width: auto;
				}
			}
		}
	}
</style>
