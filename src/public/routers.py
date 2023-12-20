from fastapi import APIRouter

public_router = APIRouter()

@public_router.get("/")
async def start():
    return {"message": "Hello app"}