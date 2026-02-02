# 🖥️ Desktop Frontend – Chemical Equipment Parameter Visualizer

This Desktop Application is part of the **FOSSEE Internship Screening Task**.  
It provides a native GUI for uploading chemical equipment data, fetching analytics from the backend, and visualizing results using charts.

The desktop app uses the **same Django backend API** as the web frontend, ensuring a true **hybrid Web + Desktop architecture**.

---

## 📌 Project Overview

The Desktop Frontend is built using **PyQt5** and **Matplotlib**.  
It allows users to:

- Upload CSV files
- Fetch dataset history
- Visualize analytics using charts

All data processing and storage are handled by the Django backend.

---

## 🧰 Tech Stack

| Layer | Technology |
|-----|-----------|
| GUI Framework | PyQt5 |
| Charts | Matplotlib |
| API Communication | Requests |
| Backend | Django REST Framework |
| Authentication | Basic Authentication |
| Database | SQLite |

---

## ✨ Features Implemented

- CSV upload to backend
- Dataset history fetch
- Equipment type distribution chart
- Average parameter visualization
- Automatic refresh after upload
- Same backend API used by Web frontend
- Clean and simple UI for demonstration

---

## 📄 CSV Format Required

The uploaded CSV file **must contain** the following columns:
# 🖥️ Desktop Frontend – Chemical Equipment Parameter Visualizer

This Desktop Application is part of the **FOSSEE Internship Screening Task**.  
It provides a native GUI for uploading chemical equipment data, fetching analytics from the backend, and visualizing results using charts.

The desktop app uses the **same Django backend API** as the web frontend, ensuring a true **hybrid Web + Desktop architecture**.

---

## 📌 Project Overview

The Desktop Frontend is built using **PyQt5** and **Matplotlib**.  
It allows users to:

- Upload CSV files
- Fetch dataset history
- Visualize analytics using charts

All data processing and storage are handled by the Django backend.

---

## 🧰 Tech Stack

| Layer | Technology |
|-----|-----------|
| GUI Framework | PyQt5 |
| Charts | Matplotlib |
| API Communication | Requests |
| Backend | Django REST Framework |
| Authentication | Basic Authentication |
| Database | SQLite |

---

## ✨ Features Implemented

- CSV upload to backend
- Dataset history fetch
- Equipment type distribution chart
- Average parameter visualization
- Automatic refresh after upload
- Same backend API used by Web frontend
- Clean and simple UI for demonstration

---

## 📄 CSV Format Required

The uploaded CSV file **must contain** the following columns:

# 🖥️ Desktop Frontend – Chemical Equipment Parameter Visualizer

This Desktop Application is part of the **FOSSEE Internship Screening Task**.  
It provides a native GUI for uploading chemical equipment data, fetching analytics from the backend, and visualizing results using charts.

The desktop app uses the **same Django backend API** as the web frontend, ensuring a true **hybrid Web + Desktop architecture**.

---

## 📌 Project Overview

The Desktop Frontend is built using **PyQt5** and **Matplotlib**.  
It allows users to:

- Upload CSV files
- Fetch dataset history
- Visualize analytics using charts

All data processing and storage are handled by the Django backend.

---

## 🧰 Tech Stack

| Layer | Technology |
|-----|-----------|
| GUI Framework | PyQt5 |
| Charts | Matplotlib |
| API Communication | Requests |
| Backend | Django REST Framework |
| Authentication | Basic Authentication |
| Database | SQLite |

---

## ✨ Features Implemented

- CSV upload to backend
- Dataset history fetch
- Equipment type distribution chart
- Average parameter visualization
- Automatic refresh after upload
- Same backend API used by Web frontend
- Clean and simple UI for demonstration

---

## 📄 CSV Format Required

The uploaded CSV file **must contain** the following columns:
Equipment Name
Type
Flowrate
Pressure
Temperature


A sample CSV is available in the root repository:



sample_equipment_data.csv


---

## 🚀 Setup Instructions

### 1️⃣ Navigate to Desktop Frontend Directory

```bash
cd desktop-frontend

2️⃣ Create Virtual Environment
python -m venv env


Activate the environment:

Windows

env\Scripts\activate


Linux / macOS

source env/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start Backend Server (Mandatory)

The Django backend must be running before starting the desktop app:

cd backend
python manage.py runserver


Backend URL:

http://127.0.0.1:8000/

5️⃣ Run Desktop Application
python main.py

🔐 Authentication

Backend APIs are protected using Basic Authentication

Desktop app communicates with authenticated APIs

Ensure a Django superuser exists

Create superuser if required:

python manage.py createsuperuser

🔌 Backend APIs Used
Endpoint	Method	Description
/api/upload/	POST	Upload CSV file
/api/history/	GET	Fetch last 5 datasets
📊 UI Components

Upload CSV button

Status message (success/failure)

Equipment Type Distribution (Bar Chart)

Average Flowrate, Pressure, Temperature (Bar Chart)

Charts update automatically after successful upload.

🧪 Testing

Upload sample_equipment_data.csv

Verify charts update correctly

Stop backend → app shows connection error (expected behavior)

📌 Notes

Backend must be running before launching desktop app

SQLite stores only the last 5 datasets

Desktop app shares backend with Web frontend

Designed for clarity, evaluation, and internship screening

🧑‍💻 Author

Sohom Bose
FOSSEE Internship Applicant
