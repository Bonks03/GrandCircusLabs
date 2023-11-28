from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random

app = FastAPI()

@app.get("/oven")
async def get_oven_temperature():
    temperature = random.randint(250, 500)
    return JSONResponse(content={'temperature': temperature})
