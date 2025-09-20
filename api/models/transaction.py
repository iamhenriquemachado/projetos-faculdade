from datetime import datetime
from helpers.uuid_generator import generateUUID
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Transaction(BaseModel):
    transacao_id: Optional[UUID] = generateUUID()
    tipo_transacao: int
    valor: float
    data_transacao: Optional[str] = datetime.now()
