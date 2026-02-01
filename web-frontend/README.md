# 🌐 Web Frontend – Chemical Equipment Parameter Visualizer

This is the **Web Frontend** for the **Chemical Equipment Parameter Visualizer**, developed as part of the **FOSSEE Internship Screening Task**.

The application allows users to upload CSV files, visualize chemical equipment analytics, and view historical datasets using charts and summary cards.

---

## 🧰 Tech Stack

- **Framework:** React.js
- **Charts:** Chart.js
- **HTTP Client:** Axios
- **Styling:** CSS (Custom Styling)
- **Backend:** Django REST Framework

---

## ✨ Features

- CSV upload interface
- Summary cards for quick analytics
- Bar charts for:
  - Equipment type distribution
  - Average flowrate, pressure, and temperature
- Dataset history synced with backend
- Authenticated API access

---

## 🚀 Setup Instructions

### 1️⃣ Install Dependencies
```bash
npm install
2️⃣ Start Development Server
npm start
Frontend will run at:

http://localhost:3000/
🔗 Backend Dependency
Ensure the backend server is running at:

http://127.0.0.1:8000/
APIs used:

/api/upload/

/api/history/

/api/report/<id>/

🧪 Testing
Upload sample_equipment_data.csv

Verify charts and summary update automatically

Ensure authentication is working

📌 Notes
Backend must be running before starting frontend

Charts update dynamically after CSV upload

Same backend is shared with Desktop frontend

🧑‍💻 Author
Sohom Bose
FOSSEE Internship Applicant
