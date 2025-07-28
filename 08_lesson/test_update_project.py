import requests
import uuid

def test_update_project_positive(headers):
    # Сначала создаём проект
    create = requests.post(BASE_URL, headers=headers, json={"name": "Old Name"})
    project_id = create.json()["id"]

    update_data = {"name": "New Name"}
    response = requests.put(f"{BASE_URL}/{project_id}", headers=headers, json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"

def test_update_project_negative(headers):
    response = requests.put(f"{BASE_URL}/invalid_id", headers=headers, json={"name": "Fail"})
    assert response.status_code in (400, 404)
