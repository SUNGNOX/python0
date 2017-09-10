import pickle
import json
print('**************pickle******************')
b = {'json': 'Job', 'age': 25, 'sex': 'boy'}
print('序列化： ',pickle.dumps(b))
po = open('json.txt', 'wb')
pickle.dump(b, po)
po.close()
pi = open('json.txt', 'rb')
mp = pickle.load(pi)
print('反序列化： ',mp)
pi.close()

print('**************json******************')
f = open('json.txt', 'w')
d = dict(a=1, b=2, c=3)
print('序列化： ',json.dumps(d))
json.dump(d, f)
f.close()
f0 = open('json.txt', 'r')
b = '{"json": "Job", "age": 25, "sex": "boy"}'
t = json.loads(b)
print('反序列化： ',t)
f.close()
