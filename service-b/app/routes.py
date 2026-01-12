from fastapi import APIRouter

from .schemas import Item
from .storage import get_item, set_item

router = APIRouter()

@router.get('/')
def root():
    return {'status': 'healthy'}

@router.post('/items/')
def add_item(item: Item):
    set_item(item.id, item.data)