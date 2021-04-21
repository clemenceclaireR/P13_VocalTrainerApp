$(function () {
  var $scoreChart = $("#score_chart");
  console.log($scoreChart.data("url"));
  $.ajax({
    url: $scoreChart.data("url")
    , success: function (data) {

    var ctx = $scoreChart[0].getContext("2d");

    moment.locale("fr");

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data.labels,
        datasets: [{
        label: 'Score',
        backgroundColor: 'blue',
        data: data.data
      }]
    },

    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true,
             max: 8
          }
        }]
      },
      responsive: true,
      legend: {
        position: 'top',
      },

      title: {
        display: true,
        text: 'Score Bar Chart'
      }
      }
      });
    }
  });
});