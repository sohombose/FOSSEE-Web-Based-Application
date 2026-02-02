# 🧪 Chemical Equipment Parameter Visualizer  
### Hybrid Web + Desktop Application

This project is developed as part of the **FOSSEE Internship Screening Task (IIT Bombay)**.  
It is a **hybrid application** consisting of:

- 🌐 **Web Application (React.js)**
- 🖥️ **Desktop Application (PyQt5)**
- ⚙️ **Common Backend (Django REST Framework)**

The system allows users to upload CSV files containing chemical equipment data, perform analytics, visualize results, maintain dataset history, and securely access APIs using authentication.

---

## 📌 Project Objectives

- Build a **single backend** serving both Web and Desktop clients
- Perform **CSV-based analytics** using Pandas
- Visualize results using:
  - Chart.js (Web)
  - Matplotlib (Desktop)
- Maintain **last 5 uploaded datasets**
- Implement **secure API access**
- Demonstrate **industry-level architecture & code structure**

---

## 🧩 System Architecture

# 🧪 Chemical Equipment Parameter Visualizer  
### Hybrid Web + Desktop Application

This project is developed as part of the **FOSSEE Internship Screening Task (IIT Bombay)**.  
It is a **hybrid application** consisting of:

- 🌐 **Web Application (React.js)**
- 🖥️ **Desktop Application (PyQt5)**
- ⚙️ **Common Backend (Django REST Framework)**

The system allows users to upload CSV files containing chemical equipment data, perform analytics, visualize results, maintain dataset history, and securely access APIs using authentication.

---

## 📌 Project Objectives

- Build a **single backend** serving both Web and Desktop clients
- Perform **CSV-based analytics** using Pandas
- Visualize results using:
  - Chart.js (Web)
  - Matplotlib (Desktop)
- Maintain **last 5 uploaded datasets**
- Implement **secure API access**
- Demonstrate **industry-level architecture & code structure**

---

## 🧩 System Architecture

                ┌───────────────────────┐
                │   React Web Frontend   │
                │   (Chart.js)           │
                └──────────┬────────────┘
                           │
                           │ REST APIs
                           │
                ┌──────────▼────────────┐
                │   Django Backend       │
                │   (DRF + Pandas)       │
                │   Auth + PDF           │
                └──────────┬────────────┘
                           │
                           │ REST APIs
                           │
                ┌──────────▼────────────┐
                │   PyQt5 Desktop App    │
                │   (Matplotlib)         │
                └───────────────────────┘


---

## 🧰 Tech Stack

### Backend
- **Django**
- **Django REST Framework**
- **Pandas**
- **SQLite**
- **Basic Authentication**
- **ReportLab (PDF Generation)**

### Web Frontend
- **React.js**
- **Chart.js**
- **Axios**

### Desktop Frontend
- **PyQt5**
- **Matplotlib**
- **Requests**

---

## ✨ Features Implemented

### 🔹 Backend
- CSV upload API
- Data validation & analytics
- Summary statistics:
  - Total equipment count
  - Average flowrate, pressure, temperature
  - Equipment type distribution
- Dataset history (last 5 uploads only)
- Secure APIs using Basic Authentication
- PDF report generation
- Shared API for Web & Desktop clients

---

### 🔹 Web Frontend (React)
- CSV upload interface
- Dataset history display
- Summary cards
- Interactive charts (Chart.js)
- Real-time updates after upload
- Clean and responsive UI

---

### 🔹 Desktop Frontend (PyQt5)
- CSV upload via file dialog
- Backend API integration
- Equipment type distribution chart
- Average parameters chart
- Shared backend with web frontend
- Clean and readable desktop UI

---

## 📄 CSV Format Required

Uploaded CSV files **must contain** the following columns:

Equipment Name
Type
Flowrate
Pressure
Temperature


A sample CSV file is provided in the repository:

sample_equipment_data.csv



---

## 📁 Project Structure

chemical-equipment-visualizer/
│
├── backend/
│ ├── config/
│ ├── equipment/
│ ├── manage.py
│ ├── requirements.txt
│
├── web-frontend/
│ ├── src/
│ ├── package.json
│
├── desktop-frontend/
│ ├── main.py
│ ├── api.py
│ ├── charts.py
│ ├── requirements.txt
│
├── sample_equipment_data.csv
└── README.md


---

## 🚀 Setup Instructions

---

## 🔹 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Backend runs at:

http://127.0.0.1:8000/

🔹 Web Frontend Setup
cd web-frontend
npm install
npm start


Web app runs at:

http://localhost:3000/

##🔹 Desktop Frontend Setup
cd desktop-frontend
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python main.py

##🔐 Authentication

All backend APIs are protected using Basic Authentication

Web & Desktop clients authenticate using backend credentials

Superuser is required to access APIs

##🔌 API Endpoints
Endpoint	Method	Description
/api/upload/	POST	Upload CSV file
/api/history/	GET	Fetch last 5 datasets
/api/report/<id>/	GET	Download PDF report
🧪 Testing

APIs tested using Postman

Web frontend tested via browser

Desktop frontend tested via PyQt application

Sample CSV used for analytics verification

##📌 Notes

SQLite used for simplicity (as per task requirement)

Old datasets are automatically deleted when count exceeds 5

Backend is shared across Web and Desktop frontends

Project follows clean code & modular architecture
