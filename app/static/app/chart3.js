Highcharts.chart('container3', {
    
        chart: {
            type: 'column',
            backgroundColor:'rgba(255, 255, 255, 0.0)'
        },
        title: {
            text: 'Evaporação Mensal'
        },
    
        subtitle: {
            text: '1912 a 2012'
        },
    
        yAxis: {
            title: {
                text: 'mm'
            }
        },
        xAxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },
        series: series_3
    
    });
    