from fastapi import FastAPI, APIRouter


from routes import router

app = FastAPI()

app.include_router(router)