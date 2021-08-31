def swap_case(h):
    g = ""
    for b in h:
        if b.isupper():
           # print("print b is upper  :",b)
            b = b.lower()
           # print("print b lower  :",b)
        else:
            b.islower()
           # print("priunt b is lower",b)
            b = b.upper()
           # print("print b upper  :",b)
        g+=g.join(b)
       # print("print g+ print  :",g)
    return g

reddy = "malapati PRATHAPREDDY"
result = swap_case(reddy)
print(result)

#count number of in a list
vol = [1,2,3,43,43,23,233]
print(vol)
vb = vol.count(43)
print(vb)

gv = [2,3,2,32,32,3223,23,23,23,2323,2]
v = 23
c = 0
for g in gv:
  #  print("print g  :",g)
    if (g==v):
        c= c+1
        print(" print c   :",c)
print("print 23 how many times in a list  :",c)

hj = [4,5,4,54,53,543,5]
v = 0
for d in hj:
    v = v+1
print("print list in a list  :",v)

german = [34,4,34]
gh = 1
for g in german:
    gh = gh*g
print(gh)





