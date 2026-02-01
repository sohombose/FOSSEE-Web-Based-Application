import React, { useEffect, useState } from "react";
import { fetchHistory } from "../services/api";
import Charts from "./Charts";
import SummaryCards from "./SummaryCards";

const DatasetHistory = ({ refresh }) => {
  const [datasets, setDatasets] = useState([]);

  const loadHistory = async () => {
    try {
      const response = await fetchHistory();
      setDatasets(response.data);
    } catch (error) {
      console.error("Error fetching history", error);
    }
  };

  useEffect(() => {
    loadHistory();
  }, [refresh]);

  return (
    <div
      style={{
        backgroundColor: "#ffffff",
        padding: "20px",
        borderRadius: "12px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
        marginBottom: "30px",
      }}
    >
      <h3>Dataset History</h3>

      {datasets.length === 0 && <p>No datasets uploaded yet.</p>}

      {datasets.length > 0 && (
        <>
          {/* Summary + Charts (latest dataset) */}
          <SummaryCards summary={datasets[0].summary} />
          <Charts summary={datasets[0].summary} />

          {/* Dataset List */}
          <div style={{ marginTop: "25px" }}>
            <h4>Uploaded Files</h4>

            <ul style={{ paddingLeft: "16px" }}>
              {datasets.map((item) => (
                <li
                  key={item.id}
                  style={{
                    marginBottom: "12px",
                    lineHeight: "1.6",
                  }}
                >
                  <strong>{item.file_name}</strong>

                  <br />
                  Total Equipment: {item.summary.total_equipment}

                  <br />

                  <button
                    style={{
                      marginTop: "6px",
                      padding: "6px 12px",
                      backgroundColor: "#2ecc71",
                      color: "white",
                      border: "none",
                      borderRadius: "6px",
                      cursor: "pointer",
                      fontSize: "14px",
                    }}
                    onClick={() =>
                      window.open(
                        `http://127.0.0.1:8000/api/report/${item.id}/`,
                        "_blank"
                      )
                    }
                  >
                    Download PDF
                  </button>
                </li>
              ))}
            </ul>
          </div>
        </>
      )}
    </div>
  );
};

export default DatasetHistory;
