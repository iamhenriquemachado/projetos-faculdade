from services.database import get_connection
from fastapi import APIRouter, HTTPException
import logging
from models.message import MSG

router = APIRouter()
logger = logging.getLogger("uvicorn")

@router.get("/transaction")
async def transactions():
    return True

@router.get("/welcome")
async def checkServerConnection():
    return {f"status": True, "message": MSG.SUCCESS_DEFAULT}