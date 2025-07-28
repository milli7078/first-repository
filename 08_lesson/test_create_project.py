import requests
import uuid

BASE_URL = "https://yougile.com/api-v2/projects"

def test_create_project_positive(headers):
    data = {
        "name": f"Test Project {uuid.uuid4()}",
        "color": "#FF5733"
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_create_project_negative(headers):
    data = {
        "color": "#FF5733"  # нет поля name (обязательное)
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    assert response.status_code == 400
