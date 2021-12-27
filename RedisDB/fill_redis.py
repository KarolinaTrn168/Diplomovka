import redis
import connection_redis

uncleanedEndpoints = open ('LearningMode/working_endpoints.txt', 'r')
for x in uncleanedEndpoints:
    print