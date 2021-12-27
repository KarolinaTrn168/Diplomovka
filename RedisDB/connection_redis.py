import redis
import json

def connection_redis():
    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)
    try:
        r = redis.Redis(host=Config['redis']['host_redis'], port=Config['redis']['port_redis'], db=Config['redis']['db_redis'])
        r.ping()
        print('Redis connected.')
    except Exception as ex:
        print('Error', ex)
        exit('Failed.')
    # r.set('dictionary.com', 'https://www.dictionary.com/')
    # r.delete('dictionary.com')
    # print(r.keys())
    return r      
        
connection_redis()