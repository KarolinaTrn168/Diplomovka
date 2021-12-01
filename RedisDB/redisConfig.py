import redis

# print(dir(redis))
r = redis.Redis(host='localhost', port=6379, db=0)
# r.set('dictionary.com', 'https://www.dictionary.com/')
r.delete('https://petstore.swagger.io/v2')

# print(r.get('https://petstore.swagger.io/v2'))