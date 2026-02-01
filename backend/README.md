# 📘 Backend – Chemical Equipment Parameter Visualizer

This backend is part of the **FOSSEE Internship Screening Task**.  
It provides REST APIs for uploading chemical equipment data, generating analytics, maintaining dataset history, and securing access using authentication.

---

## 🧰 Tech Stack

- **Framework:** Django  
- **API:** Django REST Framework  
- **Data Processing:** Pandas  
- **Database:** SQLite  
- **Authentication:** Basic Authentication  
- **PDF Generation:** ReportLab  

---

## 📂 Features Implemented

- CSV upload API for chemical equipment data  
- Automatic data validation and analytics computation  
- Summary statistics (total count, averages, type distribution)  
- Dataset history management (stores **last 5 uploads only**)  
- Secure API access using **Basic Authentication**  
- PDF report generation from stored dataset  

---

## 📄 CSV Format Required

The uploaded CSV file **must contain the following columns**:

- Equipment Name  
- Type  
- Flowrate  
- Pressure  
- Temperature  

A sample CSV file is provided in the repository root:

# 📘 Backend – Chemical Equipment Parameter Visualizer

This backend is part of the **FOSSEE Internship Screening Task**.  
It provides REST APIs for uploading chemical equipment data, generating analytics, maintaining dataset history, and securing access using authentication.

---

## 🧰 Tech Stack

- **Framework:** Django  
- **API:** Django REST Framework  
- **Data Processing:** Pandas  
- **Database:** SQLite  
- **Authentication:** Basic Authentication  
- **PDF Generation:** ReportLab  

---

## 📂 Features Implemented

- CSV upload API for chemical equipment data  
- Automatic data validation and analytics computation  
- Summary statistics (total count, averages, type distribution)  
- Dataset history management (stores **last 5 uploads only**)  
- Secure API access using **Basic Authentication**  
- PDF report generation from stored dataset  

---

## 📄 CSV Format Required

The uploaded CSV file **must contain the following columns**:

- Equipment Name  
- Type  
- Flowrate  
- Pressure  
- Temperature  

A sample CSV file is provided in the repository root:

sample_equipment_data.csv


---

## 🚀 Setup Instructions

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv

Activate Virtual Environment

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Database Migrations
python manage.py migrate

4️⃣ Create Superuser (For Authentication)
python manage.py createsuperuser

5️⃣ Start Development Server
python manage.py runserver


Backend will run at:

http://127.0.0.1:8000/

🔐 Authentication

All APIs are protected using Basic Authentication

Use Django superuser credentials to access the APIs

Authentication is required for both Web and Desktop clients

🔌 API Endpoints
📤 Upload CSV
POST /api/upload/


Auth: Required

Body Type: multipart/form-data

Key: file (CSV file)

📜 Dataset History
GET /api/history/


Auth: Required

Returns the last 5 uploaded datasets with summary analytics

📄 PDF Report
GET /api/report/<dataset_id>/


Auth: Required

Downloads a PDF analytics report for the selected dataset

🧪 Testing

APIs can be tested using:

Postman

Browser (for GET endpoints)

Web Frontend

Desktop Frontend (PyQt5)

📌 Notes

Old datasets are automatically deleted when dataset count exceeds 5

SQLite is used for simplicity as per task requirement

This backend is shared by both Web and Desktop frontends

🧑‍💻 Author

Sohom Bose
FOSSEE Internship Applicant


