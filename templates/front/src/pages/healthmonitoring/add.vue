<template>
	<div class="add-update-preview">
		<el-form
			class="add-update-form"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="80px"
			>
			<el-form-item class="add-item" label="用户ID" prop="user">
				<el-input v-model="ruleForm.user" 
					placeholder="用户ID" clearable :disabled=" false  ||ro.user"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="性别" prop="gender">
				<el-input v-model="ruleForm.gender" 
					placeholder="性别" clearable :disabled=" false  ||ro.gender"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="年龄" prop="nianling">
				<el-input v-model="ruleForm.nianling" 
					placeholder="年龄" clearable :disabled=" false  ||ro.nianling"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="身高(cm)" prop="shengao">
				<el-input v-model="ruleForm.shengao" 
					placeholder="身高(cm)" clearable :disabled=" false  ||ro.shengao"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="体重(kg)" prop="tizhong">
				<el-input v-model="ruleForm.tizhong" 
					placeholder="体重(kg)" clearable :disabled=" false  ||ro.tizhong"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="收缩压(mmHg)" prop="systolicpressure">
				<el-input v-model="ruleForm.systolicpressure" 
					placeholder="收缩压(mmHg)" clearable :disabled=" false  ||ro.systolicpressure"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="舒张压(mmHg)" prop="diastolicpressure">
				<el-input v-model="ruleForm.diastolicpressure" 
					placeholder="舒张压(mmHg)" clearable :disabled=" false  ||ro.diastolicpressure"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="心率(次/分钟)" prop="heartrate">
				<el-input v-model="ruleForm.heartrate" 
					placeholder="心率(次/分钟)" clearable :disabled=" false  ||ro.heartrate"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="血氧饱和度(%)" prop="xueyangbaohedu">
				<el-input v-model="ruleForm.xueyangbaohedu" 
					placeholder="血氧饱和度(%)" clearable :disabled=" false  ||ro.xueyangbaohedu"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="血糖(mmol/L)" prop="bloodsugar">
				<el-input v-model="ruleForm.bloodsugar" 
					placeholder="血糖(mmol/L)" clearable :disabled=" false  ||ro.bloodsugar"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="体温(℃)" prop="tiwen">
				<el-input v-model="ruleForm.tiwen" 
					placeholder="体温(℃)" clearable :disabled=" false  ||ro.tiwen"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="运动步数(步)" prop="yundongbushu">
				<el-input v-model="ruleForm.yundongbushu" 
					placeholder="运动步数(步)" clearable :disabled=" false  ||ro.yundongbushu"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="睡眠时长(小时)" prop="sleepduration">
				<el-input v-model="ruleForm.sleepduration" 
					placeholder="睡眠时长(小时)" clearable :disabled=" false  ||ro.sleepduration"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="睡眠质量评分" prop="shuimianzhiliangpingfen">
				<el-input v-model="ruleForm.shuimianzhiliangpingfen" 
					placeholder="睡眠质量评分" clearable :disabled=" false  ||ro.shuimianzhiliangpingfen"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="运动频率(次/周)" prop="yundongpinlv">
				<el-input v-model="ruleForm.yundongpinlv" 
					placeholder="运动频率(次/周)" clearable :disabled=" false  ||ro.yundongpinlv"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="饮酒习惯" prop="yinjiuxiguan">
				<el-input v-model="ruleForm.yinjiuxiguan" 
					placeholder="饮酒习惯" clearable :disabled=" false  ||ro.yinjiuxiguan"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="吸烟习惯" prop="xiyanxiguan">
				<el-input v-model="ruleForm.xiyanxiguan" 
					placeholder="吸烟习惯" clearable :disabled=" false  ||ro.xiyanxiguan"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="慢性病史" prop="manxingbingshi">
				<el-input v-model="ruleForm.manxingbingshi" 
					placeholder="慢性病史" clearable :disabled=" false  ||ro.manxingbingshi"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="家族遗传病史" prop="jiazuyichuanbingshi">
				<el-input v-model="ruleForm.jiazuyichuanbingshi" 
					placeholder="家族遗传病史" clearable :disabled=" false  ||ro.jiazuyichuanbingshi"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="健康状态" prop="healthstatus">
				<el-input v-model="ruleForm.healthstatus" 
					placeholder="健康状态" clearable :disabled=" false  ||ro.healthstatus"></el-input>
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
					user : false,
					gender : false,
					nianling : false,
					shengao : false,
					tizhong : false,
					systolicpressure : false,
					diastolicpressure : false,
					heartrate : false,
					xueyangbaohedu : false,
					bloodsugar : false,
					tiwen : false,
					yundongbushu : false,
					sleepduration : false,
					shuimianzhiliangpingfen : false,
					yundongpinlv : false,
					yinjiuxiguan : false,
					xiyanxiguan : false,
					manxingbingshi : false,
					jiazuyichuanbingshi : false,
					healthstatus : false,
				},
				type: '',
				userTableName: localStorage.getItem('UserTableName'),
				ruleForm: {
					user: '',
					gender: '',
					nianling: '',
					shengao: '',
					tizhong: '',
					systolicpressure: '',
					diastolicpressure: '',
					heartrate: '',
					xueyangbaohedu: '',
					bloodsugar: '',
					tiwen: '',
					yundongbushu: '',
					sleepduration: '',
					shuimianzhiliangpingfen: '',
					yundongpinlv: '',
					yinjiuxiguan: '',
					xiyanxiguan: '',
					manxingbingshi: '',
					jiazuyichuanbingshi: '',
					healthstatus: '',
				},


				rules: {
					user: [
					],
					gender: [
					],
					nianling: [
					],
					shengao: [
					],
					tizhong: [
					],
					systolicpressure: [
					],
					diastolicpressure: [
					],
					heartrate: [
					],
					xueyangbaohedu: [
					],
					bloodsugar: [
					],
					tiwen: [
					],
					yundongbushu: [
					],
					sleepduration: [
					],
					shuimianzhiliangpingfen: [
					],
					yundongpinlv: [
					],
					yinjiuxiguan: [
					],
					xiyanxiguan: [
					],
					manxingbingshi: [
					],
					jiazuyichuanbingshi: [
					],
					healthstatus: [
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
						if(o=='user'){
							this.ruleForm.user = obj[o];
							this.ro.user = true;
							continue;
						}
						if(o=='gender'){
							this.ruleForm.gender = obj[o];
							this.ro.gender = true;
							continue;
						}
						if(o=='nianling'){
							this.ruleForm.nianling = obj[o];
							this.ro.nianling = true;
							continue;
						}
						if(o=='shengao'){
							this.ruleForm.shengao = obj[o];
							this.ro.shengao = true;
							continue;
						}
						if(o=='tizhong'){
							this.ruleForm.tizhong = obj[o];
							this.ro.tizhong = true;
							continue;
						}
						if(o=='systolicpressure'){
							this.ruleForm.systolicpressure = obj[o];
							this.ro.systolicpressure = true;
							continue;
						}
						if(o=='diastolicpressure'){
							this.ruleForm.diastolicpressure = obj[o];
							this.ro.diastolicpressure = true;
							continue;
						}
						if(o=='heartrate'){
							this.ruleForm.heartrate = obj[o];
							this.ro.heartrate = true;
							continue;
						}
						if(o=='xueyangbaohedu'){
							this.ruleForm.xueyangbaohedu = obj[o];
							this.ro.xueyangbaohedu = true;
							continue;
						}
						if(o=='bloodsugar'){
							this.ruleForm.bloodsugar = obj[o];
							this.ro.bloodsugar = true;
							continue;
						}
						if(o=='tiwen'){
							this.ruleForm.tiwen = obj[o];
							this.ro.tiwen = true;
							continue;
						}
						if(o=='yundongbushu'){
							this.ruleForm.yundongbushu = obj[o];
							this.ro.yundongbushu = true;
							continue;
						}
						if(o=='sleepduration'){
							this.ruleForm.sleepduration = obj[o];
							this.ro.sleepduration = true;
							continue;
						}
						if(o=='shuimianzhiliangpingfen'){
							this.ruleForm.shuimianzhiliangpingfen = obj[o];
							this.ro.shuimianzhiliangpingfen = true;
							continue;
						}
						if(o=='yundongpinlv'){
							this.ruleForm.yundongpinlv = obj[o];
							this.ro.yundongpinlv = true;
							continue;
						}
						if(o=='yinjiuxiguan'){
							this.ruleForm.yinjiuxiguan = obj[o];
							this.ro.yinjiuxiguan = true;
							continue;
						}
						if(o=='xiyanxiguan'){
							this.ruleForm.xiyanxiguan = obj[o];
							this.ro.xiyanxiguan = true;
							continue;
						}
						if(o=='manxingbingshi'){
							this.ruleForm.manxingbingshi = obj[o];
							this.ro.manxingbingshi = true;
							continue;
						}
						if(o=='jiazuyichuanbingshi'){
							this.ruleForm.jiazuyichuanbingshi = obj[o];
							this.ro.jiazuyichuanbingshi = true;
							continue;
						}
						if(o=='healthstatus'){
							this.ruleForm.healthstatus = obj[o];
							this.ro.healthstatus = true;
							continue;
						}
					}
				}else if(type=='edit'){
					this.info()
				}
				// 获取用户信息
				this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						var json = res.data.data;
					}
				});

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
				this.$http.get(`healthmonitoring/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
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


						await this.$http.post(`healthmonitoring/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(async res => {
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
