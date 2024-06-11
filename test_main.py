from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_generate_sum_success():
    request_data = {
        "batchid": "test123",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/get-sum", json=request_data)

    assert response.status_code == 200
    response_data = response.json()

    assert response_data["batchid"] == request_data["batchid"]
    assert response_data["response"] == [3, 7]
    assert response_data["status"] == "complete"
    assert "started_at" in response_data
    assert "completed_at" in response_data


def test_generate_sum_empty_payload():
    request_data = {
        "batchid": "test123",
        "payload": []
    }
    response = client.post("/get-sum", json=request_data)

    assert response.status_code == 200
    response_data = response.json()

    assert response_data["batchid"] == request_data["batchid"]
    assert response_data["response"] == []
    assert response_data["status"] == "complete"
    assert "started_at" in response_data
    assert "completed_at" in response_data


def test_generate_sum_invalid_payload():
    request_data = {
        "batchid": "test123",
        "payload": ["string1", "string2"]  # Invalid payload
    }
    response = client.post("/get-sum", json=request_data)

    assert response.status_code == 422  # Unprocessable Entity


def test_generate_sum_partial_invalid_payload():
    request_data = {
        "batchid": "test123",
        "payload": [[1, 2], "str"]  # Partially invalid payload
    }
    response = client.post("/get-sum", json=request_data)

    assert response.status_code == 422  # Unprocessable Entity
