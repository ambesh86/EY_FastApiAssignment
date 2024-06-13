# ey_assignment
Python Assignment:
Task is to set up a FastAPI project and create an endpoint with request and response validation using Pydantic models.
Implement the logic to perform addition on input lists of integers using Python's multiprocessing pool, with appropriate error handling and logging for debugging and monitoring activities.
Write unit tests for all edge cases and scenarios.
Additionally, please organize your project structure following the MVC (Model-View-Controller) format.
> The request format should be as follows: 
{
    "batchid":"id0101",
    "payload":[[1,2],[3,4]]
}

> The response format should be as follows:
{
    "batchid":"id0101",
    "response":[3,7],
    "status":"completed",
    "started_at":"<timestamp>",
    "completed_at":"<timestamp>"
}

 
# Create virtual environments
python -m venv .venv

# install dependencies
pip install -r requirements.txt

# run the FastAPI application using Uvicorn:
uvicorn app.main:app --reload

# run the below Curl command to check in postman
curl -X POST "http://127.0.0.1:8000/api/v1/addition/add" -H "Content-Type: application/json" -d '{
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
}'
