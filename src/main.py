from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.products.routes import routes as products_routes
from src.users.routes import routes as users_routes
from src.image.routes import image_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

app.include_router(
    router=image_router,
    prefix="/api/v1",
    tags=["images"],
)


app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("pages/login.html", {"request": request})
