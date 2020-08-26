import redis
pool = redis.ConnectionPool(host='127.0.0.1')
r = redis.Redis(connection_pool=pool)
r.flushall()
r.set('a', 1, 5)
r.set('b', 2)
r.hset('memo', 'a', '123')
res = r.exists('c')
if res:
    print('redis里面有c')
else:
    print('redis里面没有c')

a = r.get('c')
print(a)
