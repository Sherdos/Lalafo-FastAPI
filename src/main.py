from fastapi import FastAPI
from src.products.routes import routes as products_routes
from src.users.routes import routes as users_routes

app = FastAPI()


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
