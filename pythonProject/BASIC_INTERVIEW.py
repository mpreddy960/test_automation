def febonic():
    a = 0
    b= 1
    while True:
        c = a
        a = b
        b = c+a
        yield c
tr = febonic()
for i in range(20):
    print(next(tr),end=" ")

#practise json file
import json
l = """{"sold":"jolk}"""
print(l)
print(type(l))
print(json.loads(l))
