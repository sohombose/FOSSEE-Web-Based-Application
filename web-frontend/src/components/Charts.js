import React from "react";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);
ChartJS.defaults.devicePixelRatio = 2;

const Charts = ({ summary }) => {
  if (!summary) return null;

  const typeData = {
    labels: Object.keys(summary.type_distribution),
    datasets: [
      {
        label: "Equipment Count",
        data: Object.values(summary.type_distribution),
        backgroundColor: "#4F46E5",
        borderRadius: 8,
        weight: "bold",
      },
    ],
  };

  const avgData = {
    labels: ["Flowrate", "Pressure", "Temperature"],
    datasets: [
      {
        label: "Average Values",
        
        data: [
          summary.averages.flowrate,
          summary.averages.pressure,
          summary.averages.temperature,
        ],
        backgroundColor: ["#22C55E", "#F59E0B", "#EF4444"],
        borderRadius: 8,
        weight: "bold",
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        labels: {
          font: { size: 14 },
          color: "#E5E7EB",
        },
      },
    },
    scales: {
      x: {
        ticks: { color: "#E5E7EB", font: { size: 13 } },
        grid: { display: false },
      },
      y: {
        ticks: { color: "#E5E7EB", font: { size: 13 } },
        grid: { color: "#374151" },
      },
    },
  };

  return (
    <div className="chart-container">
      <h2>Equipment Type Distribution</h2>
      <Bar data={typeData} options={options} />

      <h2 style={{ marginTop: "50px" }}>Average Parameters</h2>
      <Bar data={avgData} options={options} />
    </div>
  );
};

export default Charts;
