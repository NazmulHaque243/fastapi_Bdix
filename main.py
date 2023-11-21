from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

# from fastapi.middleware.cors import CORSMiddleware
# from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import requests as rq


class Item(BaseModel):
    url: str


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5500",
    "https://nazmulhaque243.github.io",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/check")
async def create_item(item: Item):

    url = item.url
    try:
        r = rq.get(url, timeout=4)
        if r.status_code == 200:
            return {"message": r.status_code, "item": item}
        return {"detail": "not sure!"}

    except Exception as e:
        raise HTTPException(status_code=404, detail="not working")


@app.get("/")
async def root():
    return {"massage": "Hello User"}
