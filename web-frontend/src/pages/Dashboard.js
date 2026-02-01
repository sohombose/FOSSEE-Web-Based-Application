import FileUpload from "../components/FileUpload";
import DatasetHistory from "../components/DatasetHistory";

const Dashboard = () => {
  return (
    <div className="main-container">
  <div className="header">
    Chemical Equipment Parameter Visualizer
  </div>

  <div className="card">
    <FileUpload />
  </div>

  <div className="card">
    <DatasetHistory />
  </div>
</div>

  );
};

export default Dashboard;

