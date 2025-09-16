from services.database import get_connection
from fastapi import APIRouter, HTTPException
import logging
from models.message import MSG

router = APIRouter()
logger = logging.getLogger("uvicorn")

@router.post("/transaction/{account_id}")
async def createNewTransaction():
    return False