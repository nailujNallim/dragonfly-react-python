from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"title": "Test Task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
