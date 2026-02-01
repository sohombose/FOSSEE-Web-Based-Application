import React from "react";

const SummaryCards = ({ summary }) => {
  if (!summary) return null;

  return (
    <div className="stats-grid">
      <div className="stat-card">
        <span>Total Equipment</span>
        <h2>{summary.total_equipment}</h2>
      </div>

      <div className="stat-card">
        <span>Avg Flowrate</span>
        <h2>{summary.averages.flowrate}</h2>
      </div>

      <div className="stat-card">
        <span>Avg Pressure</span>
        <h2>{summary.averages.pressure}</h2>
      </div>

      <div className="stat-card">
        <span>Avg Temperature</span>
        <h2>{summary.averages.temperature}</h2>
      </div>
    </div>
  );
};

export default SummaryCards;
