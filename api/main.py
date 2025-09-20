from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from controller import transaction_controller


app = FastAPI()
router = APIRouter()
API_PORT = 3000

app.include_router(transaction_controller.router, prefix="/api", tags=["api"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=API_PORT, reload=True)