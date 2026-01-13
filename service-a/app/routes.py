from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import requests
import json
import services as s

router = APIRouter()

# class Ip(BaseModel):
#     ip: str


# @router.post("/post_ip")
# def post_ip(ip: Ip):
#     raw_response = s.call_external_service
#     s.extract_relevant_data(raw_response)

@router.get("/")
def root():
    return {"status": "service a is healthy"}


@router.get("/service-b")
def health_check_b():
    response = json.loads(requests.get(url="http://b:8001/").text)
    return response