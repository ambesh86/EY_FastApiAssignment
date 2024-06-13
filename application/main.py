# Import necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from multiprocessing import Pool
from unittest.mock import MagicMock

# Create a FastAPI app
app = FastAPI()

# Define a Pydantic model for the request
class AdditionRequest(BaseModel):
    numbers: List[int]

# Define a Pydantic model for the response
class AdditionResponse(BaseModel):
    result: int

# Function to perform addition using multiprocessing pool
def perform_addition(numbers: List[int]) -> int:
    with Pool() as pool:
        return sum(pool.map(lambda x: x, numbers))

# Endpoint to perform addition
@app.post("/addition", response_model=AdditionResponse)
def addition(request: AdditionRequest):
    try:
        result = perform_addition(request.numbers)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error performing addition: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
