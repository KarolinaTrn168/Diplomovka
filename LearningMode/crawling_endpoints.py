from .RedisDB import requests
from RedisDB import connection_redis
import maybe.generateData as generateData
import re
import os

baseURL = ""

def get_endpoints():
    # crawling website 
    os.system('~/Desktop/Diplomka/crawlergo-0.4.2/cmd/crawlergo/crawlergo_cmd -c ~/Downloads/chrome-linux/chrome -t 15 https://www.dictionary.com/ > crawling_output.txt')
    # get method and URL, print into txt 
    os.system('grep -w \'GET\|POST\|PUT\|DELETE\' ./crawling_output.txt > all_endpoints.txt')
    os.system('cut -d " " -f 1-2 all_endpoints.txt | uniq -u > working_endpoints.txt')

def perform_requests():
    generateData.generate_data()
    print(generateData.data_list)
    backup_file = open("backup.txt", "a")
    backup_file.write("BaseURL: %s\n" %(baseURL))
    method = connection_redis.r.lpop(baseURL).decode('utf8')
    endpoint = connection_redis.r.lpop(baseURL).decode('utf8')
    backup_file.write("%s %s\n" %(method, endpoint))
    if method == 'GET':
        data_pattern = re.sub("{.*}", generateData.data_list[0], endpoint)
        if data_pattern:
            endpoint = data_pattern
            print(endpoint)
        requests.get_method(baseURL, endpoint)
    elif method == 'POST':
        requests.post_method()
    elif method == 'PUT':
        requests.put_method()
    elif method == 'DELETE':
        requests.delete_method()
    else:
        print("Not a valid method!")
        return os.error