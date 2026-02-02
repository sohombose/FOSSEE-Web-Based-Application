import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt
from api import upload_csv, fetch_history
from charts import ChartCanvas


class DesktopApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        self.setGeometry(200, 150, 1000, 780)

        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Title
        title = QLabel("Chemical Equipment Parameter Visualizer")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                padding: 12px;
                background-color: #f1c40f;
                border-radius: 8px;
            }
        """)
        layout.addWidget(title)

        # Upload Button
        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.setFixedHeight(45)
        self.upload_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                background-color: #3498db;
                color: white;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.upload_btn.clicked.connect(self.handle_upload)
        layout.addWidget(self.upload_btn)

        # Status Label
        self.status = QLabel("")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.status)

        # Charts
        self.type_chart = ChartCanvas("Equipment Type Distribution")
        layout.addWidget(self.type_chart)

        self.avg_chart = ChartCanvas("Average Parameters")
        layout.addWidget(self.avg_chart)

        self.setLayout(layout)
        self.load_history()

    def handle_upload(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        try:
            upload_csv(file_path)
            self.status.setText("✅ Upload successful")
            self.load_history()

        except Exception as e:
            QMessageBox.critical(self, "Upload Failed", str(e))
            self.status.setText("❌ Upload failed")

    def load_history(self):
        try:
            data = fetch_history()
        except Exception:
            self.status.setText("❌ Backend not running or unauthorized")
            return

        if not data:
            self.status.setText("ℹ️ No datasets available")
            return

        summary = data[0]["summary"]

        self.type_chart.plot_bar(
            list(summary["type_distribution"].keys()),
            list(summary["type_distribution"].values())
        )

        self.avg_chart.plot_bar(
            ["Flowrate", "Pressure", "Temperature"],
            [
                summary["averages"]["flowrate"],
                summary["averages"]["pressure"],
                summary["averages"]["temperature"]
            ]
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesktopApp()
    window.show()
    sys.exit(app.exec_())
