from fastapi import FastAPI

app = FastAPI()

API_PORT = 3000

@app.get('/welcome')
async def helloServer():
    return {"message": f"API is running on port {API_PORT}."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=API_PORT, reload=True)