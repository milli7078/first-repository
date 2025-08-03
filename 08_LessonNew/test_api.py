import requests
import pytest


@pytest.fixture
def headers():
    return {
        "Authorization": "Bearer SqHTwW7l0xxLtPH7BqHFzc9hp1uDeZRMZVkEO4wvSGafowGGpMBnfe9Qmlp4j7St",
        "Content-Type": "application/json"
    }


BASE_URL = "https://ru.yougile.com/api-v2/projects"


def test_create_project_positive(headers):
    data = {
        "title": "Test Project"
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative(headers):
    data = {
        "color": "#FF5733"  # нет поля title (обязательное)
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    assert response.status_code == 400


def test_get_project_positive(headers):
    # Сначала создаём проект
    create = requests.post(BASE_URL, headers=headers, json={"title": "Test"})
    project_id = create.json()["id"]

    response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative(headers):
    response = requests.get(f"{BASE_URL}/invalid_id", headers=headers)
    assert response.status_code in (400, 404)


def test_update_project_positive(headers):
    # Сначала создаём проект
    create = requests.post(BASE_URL, headers=headers, json={"title": "Old Name"})
    project_id = create.json()["id"]

    update_data = {"title": "New Name"}
    response = requests.put(f"{BASE_URL}/{project_id}", headers=headers, json=update_data)
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
    assert response.json()["title"] == "New Name"


def test_update_project_negative(headers):
    response = requests.put(f"{BASE_URL}/invalid_id", headers=headers, json={"title": "Fail"})
    assert response.status_code in (400, 404)