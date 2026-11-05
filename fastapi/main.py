from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "My first FastAPI project!",
        "name": "Tuvshe"
    }

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Цаас", "quantity": 10},
        {"id": 2, "name": "Үзэг", "quantity": 3},
        {"id": 3, "name": "Дэвтэр", "quantity": 7}
    ]
