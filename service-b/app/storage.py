import redis

redis_client = redis.Redis(host="redis-statefulset-0.redis-headless", port=6379, db=0)

def get_all():
    result = []
    for key in redis_client.scan_iter():
        result.append(f"{key}:{redis_client.get(key)}")
    return result

def set_item(item_id:str, lat:float, lon:float):
    item_data = {'lat': lat, 'lon': lon}
    redis_client.set(f"item_{item_id}", str(item_data))
    return {'message':f'added {item_id}:{item_data} to cache'}
