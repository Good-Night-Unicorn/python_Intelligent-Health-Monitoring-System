export default {
	baseUrl: 'http://localhost:8080/djangov5gemqq6/',
	name: '/djangov5gemqq6',
	indexNav: [
		{
			name: '健康知识',
			url: '/index/jiankangzhishi',
		},
		{
			name: '健康资讯',
			url: '/index/news'
		},
	],
	cateList: [
		{
			name: '健康资讯',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
