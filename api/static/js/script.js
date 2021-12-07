let dataTable = [['Time', 'Temperature', 'Humidity', 'CO2']];
let co2Table = [['Time', 'CO2']];
fetch('https://raspberrypi-api.herokuapp.com/api/all ', {
    
}).then(response => {
    return response.json();
  }).then(dataJson => {
      console.log(dataJson);
      let innerArr = []; 
      let innerCo = [];
        for (i in dataJson["temperature"]) {
            innerArr.push(dataJson["temperature"][i]["time_stamp"]);
            innerArr.push(dataJson["temperature"][i]["value"]);
            innerArr.push(dataJson["humidity"][i]["value"]);    
            innerArr.push(dataJson["co2"][i]["value"]);
            dataTable.push(innerArr);
            innerArr = [];
        }
        for (i in dataJson["co2"]) {
            innerCo.push(dataJson["co2"][i]["time_stamp"]);
            innerCo.push(dataJson["co2"][i]["value"]);
            co2Table.push(innerCo);
            innerCo = [];
        }
      console.log(co2Table);
  })
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawVisualization);
google.charts.setOnLoadCallback(drawChart);
function drawVisualization() {
var data = google.visualization.arrayToDataTable(dataTable);
var options = {
    title : 'Raspberry Pie Telemetry',
    vAxis: {title: 'Indexes'},
    hAxis: {title: 'Date'},
    seriesType: 'bars',
    series: {5: {type: 'line'}}
};
var chart = new google.visualization.ComboChart(document.getElementById('complex-chart'));
chart.draw(data, options);
}
function drawChart() {
var data = google.visualization.arrayToDataTable(co2Table);
var options = {
    title: 'СO2',
    curveType: 'function',
    legend: { position: 'bottom' }
};
var chart = new google.visualization.LineChart(document.getElementById('line-chart'));
chart.draw(data, options);
}