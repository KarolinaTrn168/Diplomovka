from os import error
from RedisDB import redisConfig
from RedisDB import requests
baseURL = ""

def get_endpoints():
    global baseURL
    endpoints_file = open("/home/karo/Desktop/Diplomovka/endpoints.txt", "r")
    for endpoints in endpoints_file:
        if endpoints.startswith("baseURL:"):
            baseURL = endpoints.strip().split(' ')[1]
        else:
            endpoint = endpoints.strip().split(' ')[1]
            method = endpoints.strip().split(' ')[0]
            redisConfig.r.rpush(baseURL, method.encode('utf8'))
            redisConfig.r.rpush(baseURL, endpoint)
        
    print("============================================= \n")
    print(redisConfig.r.lrange(baseURL, 0, -1))

    perform_requests()


def perform_requests():
    backup_file = open("backup.txt", "a")
    backup_file.write("BaseURL: %s\n" %(baseURL))
    method = redisConfig.r.lpop(baseURL).decode('utf8')
    endpoint = redisConfig.r.lpop(baseURL).decode('utf8')
    backup_file.write("%s %s\n" %(method, endpoint))
    if method == 'GET':
        requests.get_method(baseURL, endpoint)
    elif method == 'POST':
        requests.post_method()
    elif method == 'PUT':
        requests.put_method()
    elif method == 'DELETE':
        requests.delete_method()
    else:
        print("Not a valid method!")
        return error