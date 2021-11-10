from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Answer":"Mai Ruu Mai Ruu"}
    