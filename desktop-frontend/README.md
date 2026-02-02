## Project Overview

The **Chemical Equipment Parameter Visualizer** is a hybrid application developed as part of the **FOSSEE Internship Screening Task (IIT Bombay)**.  
The project focuses on uploading, analyzing, and visualizing chemical equipment parameters using a common backend that serves both a web application and a desktop application.

The system processes CSV files containing chemical equipment data and provides summary analytics and visual insights.

---

## Problem Statement

Chemical plants and laboratories often deal with large datasets containing equipment parameters such as flow rate, pressure, and temperature.  
Manual analysis of such data is time-consuming and error-prone.

This project aims to:
- Automate CSV data ingestion
- Perform statistical analysis
- Provide clear visualizations
- Maintain upload history for reference

---

## Tech Stack

### Backend
- Django
- Django REST Framework
- Pandas
- SQLite

### Frontend (Planned)
- Web: React.js + Chart.js
- Desktop: PyQt5 + Matplotlib

---

## Key Features

- CSV upload through REST API
- Automatic data analysis using Pandas
- Summary statistics:
  - Total equipment count
  - Average flowrate, pressure, temperature
  - Equipment type distribution
- Dataset history storage
- Admin panel for verification
- Common backend API for both Web and Desktop clients

---

## API Endpoints

### 1. Upload CSV
**POST** `/api/upload/`

- Content type: `multipart/form-data`
- Parameter:
  - `file` → CSV file

**Response:**
- JSON summary of analyzed data

---

### 2. Dataset History
**GET** `/api/history/`

- Returns previously uploaded datasets with timestamps and analytics summary

---

## Project Structure

chemical-equipment-visualizer/
│
├── backend/
│ ├── config/
│ ├── equipment/
│ │ ├── services/
│ │ └── migrations/
│ └── manage.py
│
├── sample_data/
│ └── sample_equipment_data.csv
│
├── README.md
└── .gitignore


---

## Setup Instructions

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver