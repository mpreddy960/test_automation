c = {23:34,45:98,"reddy":"malapati","malapati":"venkataravana"}
print(c)
b = c.values()
print(b)
x = c.keys()
print(x)
s = c.get("reddy")
print(s)
m = {2:4,45:67}
c.update(m)
print("print c update   :",c)
d = c.items()
print(d)
for x,y in d:
    print("print y:",y)
    print("print x :",x)

c.fromkeys("reddy")
print("print from keys c  :",c)
n = {"reddy":45,"rk":34}
print(n)
df = n.keys()
print(df)
cv = n.get("rk")
print(cv)
n.update(c)
print(n)
n.fromkeys("reddy")
print(n)