from fastapi import FastAPI
from .public.routers import public_router

app = FastAPI()

app.include_router(public_router)