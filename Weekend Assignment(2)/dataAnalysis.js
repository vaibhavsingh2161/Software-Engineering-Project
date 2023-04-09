const fetch = require("node-fetch");

const fetchEnergyData = async (nodeId, startDate, endDate) => {
  const url = `http://localhost:3000/energy?nodeId=${nodeId}&startDate=${startDate}&endDate=${endDate}`;
  const response = await fetch(url);
  const data = await response.json();
  return data;
};

const analyzeEnergyData = (energyData) => {
  const totalEnergyConsumption = energyData.reduce((acc, data) => {
    return acc + parseInt(data.consumption);
  }, 0);

  const averageEnergyConsumption = totalEnergyConsumption / energyData.length;

  return {
    totalEnergyConsumption,
    averageEnergyConsumption,
  };
};

const nodeId = 1;
const startDate = "2022-01-01";
const endDate = "2022-12-31";

fetchEnergyData(nodeId, startDate, endDate)
  .then((energyData) => {
    const analysisResult = analyzeEnergyData(energyData);
    console.log("Analysis result:", analysisResult);
  })
  .catch((error) => console.error("Error:", error));
