import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8000/api"

# ⚠️ Use your Django superuser credentials
USERNAME = "Sohomx"
PASSWORD = "Sohom@rpsb"


def upload_csv(file_path):
    with open(file_path, "rb") as f:
        response = requests.post(
            f"{BASE_URL}/upload/",
            files={"file": f},
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )
    response.raise_for_status()
    return response.json()


def fetch_history():
    response = requests.get(
        f"{BASE_URL}/history/",
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )
    response.raise_for_status()
    return response.json()
