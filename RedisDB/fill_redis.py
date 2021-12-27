import redis
import connection_redis
from LearningMode import crawling_endpoints

print("baseURL: ", crawling_endpoints.get_baseURL())
uncleanedEndpoints = open ('LearningMode/working_endpoints.txt', 'r')
# for x in uncleanedEndpoints:
#     print x