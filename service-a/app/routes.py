from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import requests
import json



import services as s, schemas as sc

router = APIRouter()


@router.post("/post_ip")
def post_ip(ip: sc.IpData):
    raw_response = s.call_external_service
    s.extract_relevant_data(raw_response)
    

@router.get("/")
def root():
    return {"status": "service a is healthy"}


@router.get("/service-b")
def health_check_b():
    response = json.loads(requests.get(url="http://b:8001/").text)
    return response