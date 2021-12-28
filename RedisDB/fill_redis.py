import redis
import connection_redis
from LearningMode.crawling_endpoints import get_baseURL

baseURL = get_baseURL()
print(baseURL)
r = connection_redis.connection_redis()
uncleanedEndpoints = open ('LearningMode/working_endpoints.txt', 'r')
r.rpush(baseURL, uncleanedEndpoints.readline())
for x in uncleanedEndpoints:
    r.rpush(baseURL, x)

# print(r.lrange(baseURL, 0, -1))

if(r.exists(baseURL)):
    print("EXISTS!")