google.charts.load('current', {
    'packages': ['geochart']
  });
  google.charts.setOnLoadCallback(drawRegionsMap);

  function drawRegionsMap() {

    var data = google.visualization.arrayToDataTable([
      ['Country', 'Objects'],
      ['Italy', 11],
      ['United States', 10],
      ['France', 9],
      ['China', 8],
      ['India', 7],
      ['Brazil', 6],
      ['Australia', 5],
      ['Norway', 4],
      ['Morocco', 3],
      ['Malaysia', 3],
      ['Mexico', 3],
      ['Germany', 2],
      ['Ethiopia', 1],
      ['South Africa', 1],
      ['Poland', 1],

    ]);

    var options = {
    colorAxis: {colors: ['#d9f2e6','#26734d']},
    };

    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

    chart.draw(data, options);
  }
