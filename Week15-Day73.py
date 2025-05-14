from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI()

# Bài 1: Hello API
@app.get("/")
async def hello():
    return {"Hello API"}

# Bài 2: API Máy tính
@app.get("/add")
async def add(a: int, b: int):
    return a + b

@app.get("/subtract")
async def subtract(a: int, b: int):
    return a-b

@app.get("/multiply")
async def mutiply(a: int, b: int):
    return a*b

@app.get("/divide")
async def divide(a: int, b: int):
    if b == 0:
        return "Can not divide by 0"
    else: 
        return a//b

# Bài 3: API thông tin người dùng
class User(BaseModel):
    name: str
    age: str
    email: str

@app.post("/user")
async def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "is_adult": user.age>=18
    }

# Bài 4: Quản lý danh sách sản phẩm
class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    description: Optional[str] = None

products = []
current_id = 1

@app.get("/products", response_model = List[Product])
async def get_products():
    return products

@app.post("/products", response_model = Product)
async def create_product(product: Product):
    global current_id
    product.id = current_id
    current_id += 1
    products.append(product)
    return product 