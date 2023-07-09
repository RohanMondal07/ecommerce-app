from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str
    zip_code: str

class OrderItem(BaseModel):
    productId: int
    boughtQuantity: int

class Order(BaseModel):
    timestamp: str
    items: list[OrderItem]
    totalAmount: float
    address: Address

class Product(BaseModel):
    name: str
    price: float
    quantity: int
