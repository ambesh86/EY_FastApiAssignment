# test_main.py
from fastapi.testclient import TestClient
from application.main import app
from unittest.mock import patch
from datetime import datetime

client = TestClient(app)

@patch("controllers.parallel_addition")
def test_perform_addition(mock_parallel_addition):
    # Mock the parallel_addition function
    mock_parallel_addition.return_value = 10

    # Define input data
    input_data = {
        "Batched": "id01101",
        "payload": [[1, 2], [3, 4]]
    }

    # Send a POST request to the /addition/ endpoint
    response = client.post("/addition/", json=input_data)

    # Check if the response is successful
    assert response.status_code == 200
    assert response.json() == {
        "Batched": "id01101",
        "response": 10,
        "Status": "completed",
        "started_at": "2023-01-01T00:00:00",
        "completed_at": "2023-01-01T00:01:00"
    }

    # Verify that parallel_addition was called with the correct input
    mock_parallel_addition.assert_called_once_with([[1, 2], [3, 4]])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
