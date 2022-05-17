from fastapi import FastAPI
from controllers.routers import node_router
from controllers.routers import findor_router
from controllers.routers import park_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(node_router)
app.include_router(findor_router)
app.include_router(park_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return "Hello from home"
