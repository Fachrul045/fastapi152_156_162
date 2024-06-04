from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Inisialisasi FastAPI
app = FastAPI()

# Definisikan model data untuk baju
class Shirt(BaseModel):
    name: str
    brand: str
    size: str
    price: float

# Data baju sementara
shirt_db: List[Shirt] = []

# Endpoint untuk menambahkan baju baru
@app.post("/shirts/", response_model=Shirt)
async def create_shirt(shirt: Shirt):
    shirt_db.append(shirt)
    return shirt

# Endpoint untuk mendapatkan daftar semua baju
@app.get("/shirts/", response_model=List[Shirt])
async def get_all_shirts():
    return shirt_db

# Endpoint untuk mendapatkan detail baju berdasarkan ID
@app.get("/shirts/{shirt_id}", response_model=Shirt)
async def get_shirt_by_id(shirt_id: int):
    if shirt_id < 0 or shirt_id >= len(shirt_db):
        raise HTTPException(status_code=404, detail="Shirt ID not found")
    return shirt_db[shirt_id]

# Endpoint untuk memperbarui detail baju berdasarkan ID
@app.put("/shirts/{shirt_id}", response_model=Shirt)
async def update_shirt(shirt_id: int, shirt: Shirt):
    if shirt_id < 0 or shirt_id >= len(shirt_db):
        raise HTTPException(status_code=404, detail="Shirt ID not found")
    shirt_db[shirt_id] = shirt
    return shirt_db[shirt_id]

# Endpoint untuk menghapus baju berdasarkan ID
@app.delete("/shirts/{shirt_id}", response_model=Shirt)
async def delete_shirt(shirt_id: int):
    if shirt_id < 0 or shirt_id >= len(shirt_db):
        raise HTTPException(status_code=404, detail="Shirt ID not found")
    deleted_shirt = shirt_db.pop(shirt_id)
    return deleted_shirt

# Menjalankan aplikasi menggunakan Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
