from datetime import datetime
from bson import ObjectId
from fastapi import FastAPI, status, Query, HTTPException, Body
import motor.motor_asyncio
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel
import uvicorn

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://ecom123:pass1234@ecommerce.tdtbegi.mongodb.net/?retryWrites=true&w=majority")
db = client.ecommerce

class Product(BaseModel):
    name: str
    price: float
    available_quantity: int

class OrderItem(BaseModel):
    product_id: str
    bought_quantity: int

class Order(BaseModel):
    timestamp: str
    items: List[OrderItem]
    total_amount: float
    user_address: dict[str, str]

@app.get("/", response_description="Home")
async def home():
    return {"status": "ok"}

@app.get("/get-products/", response_description="List all products", response_model=List[Product])
async def list_products(limit: int = Query(10, ge=1, le=100), offset: int = Query(0, ge=0)):
    if limit < 1 or limit > 10:
        raise HTTPException(status_code=400, detail="Invalid limit. Limit must be between 1 and 100.")
    if offset < 0:
        raise HTTPException(status_code=400, detail="Invalid offset. Offset must be greater than or equal to 0.")
    products = await db["Product"].find().skip(offset).limit(limit).to_list(length=None)
    return products

@app.post("/post-products/", response_description="Add new product", response_model=Product)
async def create_product(product: Product = Body(...)):
    product = jsonable_encoder(product)
    new_product = await db["products"].insert_one(product)
    created_product = await db["products"].find_one({"_id": new_product.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_product)

@app.put("/edit-products/{product_id}", response_description="Update product")
async def update_product(product_id: str, quantity: int):
    existing_product = await db["products"].find_one({"_id": product_id})
    if not existing_product:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found.")
    await db["products"].update_one({"_id": product_id}, {"$set": {"available_quantity": quantity}})
    updated_product = await db["products"].find_one({"_id": product_id})
    return JSONResponse(status_code=status.HTTP_200_OK, content=updated_product)

@app.get("/get-orders/", response_description="List all orders", response_model=List[Order])
async def list_orders(limit: int = Query(10, ge=1, le=10), offset: int = Query(0, ge=0)):
    if limit < 1 or limit > 10:
        raise HTTPException(status_code=400, detail="Invalid limit. Limit must be between 1 and 1000.")
    if offset < 0:
        raise HTTPException(status_code=400, detail="Invalid offset. Offset must be greater than or equal to 0.")
    orders = await db["orders"].find().skip(offset).limit(limit).to_list(length=None)
    return orders

@app.get("/orders/{order_id}", response_description="Get a single order", response_model=Order)
async def get_order(order_id: str):
    order = await db["orders"].find_one({"_id": ObjectId(order_id)})
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with ID {order_id} not found.")
    return order

@app.post("/post-orders/", response_description="Add new order")
async def create_order(order: Order):
    order_dict = order.dict()
    order_dict["timestamp"] = datetime.now().isoformat()
    new_order = await db["orders"].insert_one(order_dict)
    created_order = await db["orders"].find_one({"_id": new_order.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_order)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
