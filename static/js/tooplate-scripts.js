const width_threshold = 480;

function drawLineChart() {
  if ($("#lineChart").length) {
    ctxLine = document.getElementById("lineChart").getContext("2d");
    optionsLine = {
      scales: {
        xAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "تاریخ و نام کاربر",
            },
          },
        ],
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "تعداد",
            },
          },
        ],
      },
    };

    // Set aspect ratio based on window width
    optionsLine.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configLine = {
      type: "line",
      data: {
        labels: [], // Persian dates and user names
        datasets: [
          {
            label: "تعداد فاکتورها",
            data: [], // User statistics for factors
            fill: false,
            borderColor: "rgb(75, 192, 192)",
            cubicInterpolationMode: "monotone",
            pointRadius: 0,
          },
          {
            label: "تعداد خدمات",
            data: [], // User statistics for services
            fill: false,
            borderColor: "rgba(255,99,132,1)",
            cubicInterpolationMode: "monotone",
            pointRadius: 0,
          },
        ],
      },
      options: optionsLine,
    };

    // Make an AJAX request to fetch user stats with dates and user names in Persian
    $.ajax({
      url: "/get_user_stats/", // Update with the actual URL
      method: "GET",
      success: function (data) {
        // Convert Gregorian dates to Persian using jalali-moment
        const persianLabels = data.user_stats.map((user) => {
          const gregorianDate = moment(user.date, "YYYY-MM-DD");
          const persianDate = gregorianDate.format("YYYY/MM/DD");
          return `${persianDate} - ${user.name}`;
        });

        // Update chart labels with Persian dates and user names
        configLine.data.labels = persianLabels;
        configLine.data.datasets[0].data = data.user_stats.map(
          (user) => user.num_factors
        );
        configLine.data.datasets[1].data = data.user_stats.map(
          (user) => user.num_services
        );

        // Create or update the chart
        if (lineChart) {
          lineChart.update();
        } else {
          lineChart = new Chart(ctxLine, configLine);
        }
      },
      error: function (error) {
        console.error("Error:", error);
      },
    });
  }
}

function drawBarChart() {
  // Get the start and end date from the input fields
  const startDate = $("#start_date").val();
  const endDate = $("#end_date").val();

  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        xAxes: [
          {
            stacked: true,
            ticks: {
              beginAtZero: true,
            },
          },
        ],
        yAxes: [
          {
            stacked: true,
            barPercentage: 0.2,
            scaleLabel: {
              display: true,
              labelString: "تعداد",
            },
          },
        ],
      },
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "horizontalBar",
      data: {
        labels: [],
        datasets: [],
      },
      options: optionsBar,
    };

    // Make an AJAX request to fetch data from Django with start and end dates
    $.ajax({
      url: "/bar_chart_data/", // Update with your Django URL
      type: "GET",
      dataType: "json",
      data: {
        start_date: startDate,
        end_date: endDate,
      },
      success: function (data) {
        configBar.data.labels = data.labels;
        configBar.data.datasets = data.datasets;

        barChart = new Chart(ctxBar, configBar);
      },
    });
  }
}

function drawPieChart() {
  if ($("#pieChart").length) {
    var chartHeight = 300;

    $("#pieChartContainer").css("height", chartHeight + "px");

    ctxPie = document.getElementById("pieChart").getContext("2d");

    optionsPie = {
      responsive: true,
      maintainAspectRatio: false,
      layout: {
        padding: {
          left: 10,
          right: 10,
          top: 10,
          bottom: 10,
        },
      },
      legend: {
        position: "top",
      },
    };

    // Make an AJAX request to fetch data from Django
    $.ajax({
      url: "/chart_data/", // Update with your Django URL
      type: "GET",
      dataType: "json",
      success: function (data) {
        configPie = {
          type: "pie",
          data: {
            datasets: [
              {
                data: data.data,
                backgroundColor: data.backgroundColor,
                label: "Customer Status",
              },
            ],
            labels: data.labels,
          },
          options: optionsPie,
        };

        pieChart = new Chart(ctxPie, configPie);
      },
    });
  }
}

function updateLineChart() {
  if (lineChart) {
    lineChart.options = optionsLine;
    lineChart.update();
  }
}

function updateBarChart() {
  if (barChart) {
    barChart.options = optionsBar;
    barChart.update();
  }
}
