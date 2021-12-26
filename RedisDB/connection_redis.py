import redis
import json

def connection_redis():
    with open('/home/karo/Desktop/Diplomka/Diplomovka/RedisDB/redis_config.json', encoding='utf8') as config_file:
        Config = json.load(config_file)
    try:
        # print(dir(redis))
        r = redis.Redis(host=Config['redis']['host_redis'], port=Config['redis']['port_redis'], db=Config['redis']['db_redis'])
        r.ping()
        print('Redis connected.')
    except Exception as ex:
        print('Error', ex)
        exit('Failed.')
    return r      
        
        
    # r.set('dictionary.com', 'https://www.dictionary.com/')
    # r.delete('https://petstore.swagger.io/v2')
    # print(r.get('https://petstore.swagger.io/v2'))