from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.post_routes import post_router
from app.routes.get_routes import get_router
from app.routes.delete_routes import delete_router
app = FastAPI()
app.include_router(post_router)
app.include_router(get_router)
app.include_router(delete_router)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main_route():
    return {"hello":"world"}