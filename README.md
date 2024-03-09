# Simple E-commerce Application

This is a simple e-commerce application built with FastAPI and MongoDB.

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

3. Install dependencies:
   pip install -r requirements.txt
   
4. Set up environment variables:
   Create a .env file in the root directory.
   Add your environment variables to the .env file:

# Usage
1. Start the FastAPI application:
   uvicorn main:app --reload
   Open your web browser and navigate to http://localhost:8000/ to access the application.

# Testing
1. Use Postman or curl to test the API endpoints. For example:
   curl -X POST "http://localhost:8000/buy" -H "Content-Type: application/json" -d "{\"product\":\"Product Name\"}"
   or
   Invoke-WebRequest -Uri "http://127.0.0.1:8000/report" -Method GET -Headers @{"X-Secret-Key"="your-secret-key"}

# License
  This project is licensed under the MIT License - see the LICENSE.md file for details.


