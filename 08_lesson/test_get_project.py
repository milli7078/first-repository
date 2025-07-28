import requests
import uuid

def test_get_project_positive(headers):
    # Сначала создаём проект
    create = requests.post(BASE_URL, headers=headers, json={"name": "Test"})
    project_id = create.json()["id"]

    response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_get_project_negative(headers):
    response = requests.get(f"{BASE_URL}/invalid_id", headers=headers)
    assert response.status_code in (400, 404)
