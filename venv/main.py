from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import FileResponse
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

app = FastAPI()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
sales_collection = db['sales']

# Secret key for accessing the sales report
secret_key = os.getenv("SECRET_KEY")

# Buy endpoint
@app.post("/buy")
async def buy_product(product: dict):
    # Insert the sales record into the MongoDB database
    sales_collection.insert_one(product)
    return {"message": f"Successfully purchased {product['product']}"}

# Report endpoint
# Report endpoint
@app.get("/report")
async def generate_report(X_Secret_Key: str = Header(None)):
    # Verify the secret key
    if X_Secret_Key != secret_key:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Generate sales report
    sales_report = sales_collection.aggregate([
        {"$group": {"_id": "$product", "total_sales": {"$sum": 1}}}
    ])
    report = [{"product": sale["_id"], "total_sales": sale["total_sales"]} for sale in sales_report]
    return report


# Route for serving the index.html file
@app.get("/")
async def read_index():
    return FileResponse("venv/index.html")

@app.delete("/delete")
async def delete_data():
    # Delete all documents in the sales collection
    sales_collection.delete_many({})
    return {"message": "All data deleted."}