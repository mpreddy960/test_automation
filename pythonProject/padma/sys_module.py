import sys
#print(sys.version)

# for line in sys.stdin:
#     print("going :",line.strip())
#     if 'q' == line.rstrip():
#         break
#     print(f'Input : {line}')
# print("Exit")


# stdout assigned to a variable
var = sys.stdout
arr = ['geeks', 'for', 'geeks']
# printing everything in the same line
for i in arr:
    var.write(i)
# printing everything in a new line
for j in arr:
    var.write('\n'+j)

#practice
red = sys.stdout
vol = ["fold","2",'3','23','4']
for b in vol:
    red.write('\n'+b)

sys_module = ("   helps","poor","students")
import_sys_module = sys.stdout
for stay in sys_module:
    import_sys_module.write(stay)
vo = {"reddy","colom"}
for n in vo:
    red.write("\n"+n)


def print_to_stderr(*a):

    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a,file=sys.stderr)
print_to_stderr("Hello World")

def going(b):
    print(b,file = sys.stderr)
going("malapatireddys")

def holl(v):
    print(v,file = sys.stderr)
holl("google job")

import sys
novel = sys.stdout
high = ["pop","fully","finish"]
for hold in high:
    novel.write("\n"+hold)
#practice
# red = sys.stdout
# vol = ["fold","2",'3','23','4']
# for b in vol:
#     red.write('\n'+b)
#for practice stdout
coal = sys.stdout
doll = ("culcatta","maharastra","manoj")
for union in doll:
    coal.write("\n"+union)
#for practice stderr
dell = sys.stderr
for ten in doll:
    dell.write("\n"+ten)
#stderr
def hundread(j):
    print(j,file= sys.stderr)
hundread("\n"+"tokyo")
#stderr
cool = sys.stderr
boll = ("typrerror")
for paisa in boll:
    cool.write(paisa)
goof = sys.stderr
jell = ("    erro throw")
for h in jell:
    goof.write(h)
#stdin
gel = sys.stdin
money = {"control","coaching"}

