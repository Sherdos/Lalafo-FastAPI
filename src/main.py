from fastapi import FastAPI
from src.products.routes import routes as products_routes
from src.users.routes import routes as users_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


app.include_router(
    router=products_routes,
    prefix="/api/v1",
    tags=["products"],
)

app.include_router(
    router=users_routes,
    prefix="/api/v1",
    tags=["users"],
)
