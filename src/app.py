from fastapi import FastAPI
from controllers.routers import node_router
from controllers.routers import findor_router

app = FastAPI()

app.include_router(node_router)
app.include_router(findor_router)

@app.get("/")
def read_root():
    return "Hello from home"

