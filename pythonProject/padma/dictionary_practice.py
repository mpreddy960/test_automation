c = {23:34,45:98,"reddy":"malapati","malapati":"venkataravana"}
print(c)
b = c.values()
print(b)
x = c.keys()
print(x)
s = c.get("reddy")
print("print s ;;;;;",s)
fg = c.get("malapati")
print("print fg;;;;;",fg)
m = {2:4,45:67}
c.update(m)
print("print c update   :",c)
d = c.items()
print("print d;;;;;;;",d)
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

got = {"fold":"clothes","pop":"corn"}
print("print got;;;;",got)
sd = got.get("pop")
print("get items ::::",sd)
vb = got.items()
print("pop items ::::",vb)

for i in got:
    print(i)
    rt = "-"
    i.join(rt)
    print("print rt ::::",rt)

reddy = "pop"
fg = "reddy"
reddy.join(fg)
print("print  :::",reddy)



