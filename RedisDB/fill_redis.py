import redis
import connection_redis
import LearningMode
# from LearningMode import crawling_endpoints

print("baseURL: ", LearningMode.crawling_endpoints.get_baseURL())
uncleanedEndpoints = open ('LearningMode/working_endpoints.txt', 'r')
# for x in uncleanedEndpoints:
#     print x