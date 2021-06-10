
// import the data
d3.csv("data_filtered.csv").then((importedData) => {
    var data = importedData;

    console.log(data);

    var tbody = d3.select("tbody");

data.forEach((data) => {
    var row = tbody.append("tr");
    Object.entries(data).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
})

