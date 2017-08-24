Highcharts.chart('container3', {
    
        chart: {
            type: 'column'
        },
        title: {
            text: 'Evaporação Mensal'
        },
    
        subtitle: {
            text: ''
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
    