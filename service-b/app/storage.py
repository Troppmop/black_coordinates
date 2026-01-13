import redis

redis_client = redis.Redis(host='redis', port=6379, db=0)

def get_item(item_id:str):
    cached_item = redis_client.get(f"item_{id}")

    if not cached_item:
        return {'message':'item not found'}
    
    else:
        item_data = cached_item.decode('utf-8')
    
        return {"ip": item_id, "lat": item_data['lat'], "lon": item_data['lon']}

def set_item(item_id:str, lat, lon):
    item_data = {'lat': lat, 'lon': lon}
    redis_client.setex(f"item_{item_id}", 3600, item_data)
    return {'message':f'added {item_id}:{item_data} to cache'}
