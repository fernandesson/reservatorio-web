Highcharts.chart('container1', {

	chart: {
        type: 'column',
        backgroundColor:'rgba(255, 255, 255, 0.0)'
	},
    title: {
        text: 'Vazão Média Mensal'
    },

    subtitle: {
        text: '1912 a 2012'
    },

    yAxis: {
        title: {
            text: 'm³/s'
        }
    },
	xAxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },
    series: series_1

});
