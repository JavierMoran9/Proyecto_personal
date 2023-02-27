from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.prof import prof_router
from routers.alum import alum_router
from routers.user import user_router


app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(alum_router)
app.include_router(prof_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)