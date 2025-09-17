from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from router import transaction


app = FastAPI()
router = APIRouter()
API_PORT = 3000

app.include_router(transaction.router, prefix="/api", tags=["api"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=API_PORT, reload=True)