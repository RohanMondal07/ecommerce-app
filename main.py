import uvicorn
from fastapi import FastAPI
from motor import motor_asyncio
from pydantic import BaseModel

app = FastAPI()

# MongoDB connection
client = motor_asyncio.AsyncIOMotorClient("mongodb+srv://ecom123:pass1234@ecommerce.tdtbegi.mongodb.net/")
db = client["ecommerce"]
products_collection = db["products"]
orders_collection = db["orders"]

# Models
class Product(BaseModel):
    name: str
    price: float
    available_quantity: int

class Order(BaseModel):
    timestamp: str
    items: list
    user_address: dict

# API endpoints
@app.get("/products")
async def list_products():
    products = await products_collection.find().to_list(20)
    return products

@app.post("/orders")
async def create_order(order: Order):
    order_id = await orders_collection.insert_one(order.dict()).inserted_id
    return {"order_id": str(order_id)}

@app.get("/orders")
async def fetch_orders(limit: int = 10, offset: int = 0):
    orders = await orders_collection.find().skip(offset).limit(limit).to_list(limit)
    return orders

@app.get("/orders/{order_id}")
async def fetch_order(order_id: str):
    order = await orders_collection.find_one({"_id": order_id})
    if order:
        return order
    return {"message": "Order not found"}

@app.put("/products/{product_id}")
async def update_product(product_id: str, quantity: int):
    result = await products_collection.update_one(
        {"_id": product_id},
        {"$set": {"available_quantity": quantity}}
    )
    if result.modified_count:
        return {"message": "Product updated successfully"}
    return {"message": "Product not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
