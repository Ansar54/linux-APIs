from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# GET API: Get item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# POST API: Create a new item
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created", "item": item}

# PUT API: Update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": "Item updated", "item_id": item_id, "updated_item": item}

# DELETE API: Delete an item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with ID {item_id} has been deleted"}

