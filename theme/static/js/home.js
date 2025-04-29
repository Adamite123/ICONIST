document.addEventListener("DOMContentLoaded", function () {
  var options = {
    series: [14, 23, 21, 17],
    chart: {
      type: "polarArea",
      width: 380,
    },
    fill: {
      colors: ["#8950FC", "#FFA800", "#00B5B8", "#F1416C"],
    },
    stroke: {
      colors: ["#fff"],
    },
    plotOptions: {
      polarArea: {
        rings: {
          strokeWidth: 0,
        },
        spokes: {
          strokeWidth: 0,
        },
      },
    },
    responsive: [
      {
        breakpoint: 480,
        options: {
          chart: {
            width: 100,
          },
          legend: {
            position: "bottom",
          },
        },
      },
    ],
  };

  var options2 = {
    series: [
      {
        name: "Desktops",
        data: [10, 41, 35, 51, 49, 62, 69, 91, 148],
      },
    ],
    chart: {
      height: 350,
      type: "line",
      zoom: {
        enabled: false,
      },
      markers: {
        size: 5,
        shape: "circle",
        strokeColors: "#fff",
        strokeWidth: 2,
        strokeOpacity: 0.9,
        strokeDashArray: 0,
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: "straight",
    },
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
      ],
    },
  };

  var options3 = {
    series: [
      {
        name: "PRODUCT A",
        data: [44, 55, 41, 67, 22, 43, 21, 49, 35, 50, 60, 70],
      },
      {
        name: "PRODUCT B",
        data: [13, 23, 20, 8, 13, 27, 33, 12, 25, 30, 40, 45],
      },
    ],
    chart: {
      type: "bar",
      height: 350,
      stacked: true,
    },
    plotOptions: {
      bar: {
        borderRadius: 5,
      },
    },
    colors: ["#8950FC", "#FFA800"],
    responsive: [
      {
        breakpoint: 480,
        options: {
          legend: {
            position: "bottom",
            offsetX: -10,
            offsetY: 0,
          },
        },
      },
    ],
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ],
    },
    fill: {
      opacity: 1,
    },
    legend: {
      position: "right",
      offsetX: 0,
      offsetY: 50,
    },
  };

  var chart = new ApexCharts(document.querySelector("#diagram1"), options);
  var chart2 = new ApexCharts(document.querySelector("#diagram2"), options2);
  var chart3 = new ApexCharts(document.querySelector("#diagram3"), options3);
  chart.render();
  chart2.render();
  chart3.render();
});
