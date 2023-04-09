const express = require("express");
const app = express();

app.get("/energy", (req, res) => {
  const nodeId = req.query.nodeId;
  const startDate = req.query.startDate;
  const endDate = req.query.endDate;

  const energyData = [
    { timestamp: "2022-01-01T00:00:00Z", consumption: 100 },
    { timestamp: "2022-01-02T00:00:00Z", consumption: 150 },
    { timestamp: "2022-01-03T00:00:00Z", consumption: 200 },
  ];

  res.json(energyData);
});

app.listen(3000, () => {
  console.log("API server is running on http://localhost:3000");
});
