📘 Backend – Chemical Equipment Parameter Visualizer

This backend is part of the FOSSEE Internship Screening Task.
It provides REST APIs for uploading chemical equipment data, generating analytics, maintaining dataset history, and securing access using authentication.

🧰 Tech Stack

Framework: Django

API: Django REST Framework

Data Processing: Pandas

Database: SQLite

Authentication: Basic Authentication

PDF Generation: ReportLab

📂 Features Implemented

CSV upload API for chemical equipment data

Automatic data validation and analytics computation

Summary statistics (count, averages, type distribution)

Dataset history (stores last 5 uploads only)

Secure API access using Basic Authentication

PDF report generation from stored dataset

📄 CSV Format Required

The uploaded CSV file must contain the following columns:

Equipment Name
Type
Flowrate
Pressure
Temperature


A sample file is provided in the root repository:

sample_equipment_data.csv

🚀 Setup Instructions
1️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Migrations
python manage.py migrate

4️⃣ Create Superuser (For Authentication)
python manage.py createsuperuser

5️⃣ Start Server
python manage.py runserver


Backend will run at:

http://127.0.0.1:8000/

🔐 Authentication

All APIs are protected using Basic Authentication.

Use Django superuser credentials to access APIs.

🔌 API Endpoints
Upload CSV
POST /api/upload/


Auth: Required

Body: multipart/form-data

Key: file

Dataset History
GET /api/history/


Auth: Required

Returns last 5 uploaded datasets

PDF Report
GET /api/report/<dataset_id>/


Auth: Required

Downloads PDF report for selected dataset

🧪 Testing

APIs can be tested using:

Postman

Browser (GET endpoints)

📌 Notes

Old datasets are automatically deleted when count exceeds 5

SQLite is used for simplicity as per task requirement

Backend is shared by both Web and Desktop frontends

🧑‍💻 Author

Sohom Bose
FOSSEE Internship Applicant
