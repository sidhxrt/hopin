from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/hop")
async def hop_function():
    return "hop"