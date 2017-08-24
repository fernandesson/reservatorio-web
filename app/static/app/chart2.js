Highcharts.chart('container2', {

	chart: {
		zoomType: 'x'
	},
    title: {
        text: 'Vazão'
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
		type: 'datetime',
		labels: {
            formatter: function() {
                return Highcharts.dateFormat('%m/%Y', this.value);
            }
		},
		startOnTick: true
	},
    plotOptions: {
        series: {
            pointStart: Date.UTC(1912, 0, 1),
			pointInterval: 24*3600*1000*30
        }
    },

    series: series_2

});
