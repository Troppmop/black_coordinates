from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import requests


from app import services as s, schemas as sc

router = APIRouter()


@router.post("/post_ip")
def post_ip(ip: sc.IpData):
    raw_response = s.call_external_service
    s.extract_relevant_data(raw_response)
    

@router.get("/")
def root():
    return {"status: service a is healthy"}


@router.get("/service-b")
def health_check_b():
    response = requests.get(url="localhost:8001/")
    return response