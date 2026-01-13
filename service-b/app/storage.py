"""import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_item(item_id:int):
    cached_item = redis_client.get(f"item_{id}")

    if not cached_item:
        return {'message':'item not found'}
    
    else:
        return {"item_id": item_id, "cached": True, "data": cached_item.decode('utf-8')}

def set_item(item_id:int, item_data):
    redis_client.setex(f"item_{item_id}", 3600, item_data)
    return {'message':'added'}
"""