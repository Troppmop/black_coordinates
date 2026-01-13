from fastapi import APIRouter
import requests
import json
from schemas import Item
from storage import get_all, set_item



router = APIRouter()
  
@router.get('/')
def root():
    return {'status': 'service-b is healthy'}
    

@router.get('/service-a')
def healthcheck_a():
    response = json.loads(requests.get(url='http://a:8000/').text)
    return response

@router.post('/items')
def add_item(item: Item):
    response = set_item(item.ip, item.lat, item.lon)
    return response

@router.get('/items/')
def retrieve(ip:str):
    response = get_all()
    return response