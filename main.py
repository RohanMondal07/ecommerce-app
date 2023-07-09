from fastapi import FastAPI, HTTPException
from typing import List
from models import Product, Order
from pymongo import MongoClient

app = FastAPI()

# In-memory storage for products and orders
products = []
orders = []


# Connect to MongoDB
client = MongoClient("mongodb+srv://ecom123:pass1234@ecommerce.tdtbegi.mongodb.net/")
db = client["ecommerce"]
products_collection = db["products"]
orders_collection = db["orders"]


@app.get("/products")
def get_products():
    return products

@app.post("/orders")
def create_order(order: Order):
    # Verify product availability and calculate total amount
    total_amount = 0
    for item in order.items:
        product = next((p for p in products if p.id == item.productId), None)
        if not product or item.boughtQuantity > product.quantity:
            raise HTTPException(status_code=400, detail="Insufficient quantity for product: {}".format(item.productId))

        total_amount += product.price * item.boughtQuantity

    # Save the order
    order.totalAmount = total_amount
    orders.append(order)
    return order

@app.get("/orders")
def get_orders(limit: int = 10, offset: int = 0):
    return orders[offset:offset + limit]

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    order = next((o for o in orders if o.id == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.put("/products/{product_id}")
def update_product(product_id: int, quantity: int):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.quantity = quantity
    return product
