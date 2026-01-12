from fastapi import FastAPI, APIRouter


from app.routes import router

app = FastAPI()

app.include_router(router)