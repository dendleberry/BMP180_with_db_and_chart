chart = ''

window.onload = function () {
    tryChartJs();
}

function tryChartJs(){
    var ctx = document.getElementById('myChart').getContext('2d');
    ctx.height = 1100;
    window.chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        fill: false,
        labels: ['a','b'],
        datasets: [{
            borderColor: 'rgb(111, 57, 16)',
            data: ['233' , '244'],
            label: 'Sewer Pressure'
        }]
    },

    // Configuration options go here
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [{
                ticks: {
                    autoSkip: false,
                    maxRotation: 90,
                    minRotation: 90
                }
            }]
        
    }}
    });
    getRealData('http://192.168.0.22:80/get');
    window.chart.update();
}

function getRealData(url) {
    fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data_response) => {
        labels_out = data_response.labels;
        data_out = data_response.data;
        window.chart.data.labels = labels_out;
        window.chart.data.datasets[0].data = data_out;
        window.chart.data.datasets[0].label = 'Sewer Pressure - ' + window.chart.data.labels[0] + ' - ' + window.chart.data.labels[window.chart.data.labels.length-1]
        window.chart.update();
    });
}

function handleClick(){
    var fromDate = document.getElementById("fromDate").value;
    var toDate = document.getElementById("toDate").value;
    var fromDateAsDate = new Date(fromDate);
    var toDateAsDate = new Date(toDate);
    if (isNaN(fromDateAsDate) && fromDate != "") {
        alert(fromDate + ' is not in the correct format (YYYY-MMM-DD HH:MM:SS).')
        return;
    }
    if (isNaN(toDateAsDate) && toDate != "") {
        alert(toDate + ' is not in the correct format (YYYY-MMM-DD HH:MM:SS).')
        return;
    }
    getRealData('http://192.168.0.22:80/get?from='+fromDate+'&to='+toDate);
    window.chart.update();
}

