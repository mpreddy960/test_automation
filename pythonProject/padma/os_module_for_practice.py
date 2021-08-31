import os
reddy = os.getcwd()
print("print current path :",reddy)
#chaging path
def new_path():
    print(os.getcwd())

print("print before path")
new_path()
os.chdir("../")
print("after path")
new_path()
#makedirs[create a new directory]
try:
    ganga = "malapatiprathapreddy"
    bottle = os.getcwd()
    print(bottle)
    fell = bottle+"/reddy/looking/lock"
    wall =os.path.join(fell,ganga)
    os.makedirs(wall)
except FileExistsError:
    pass
#added new path
life = "lingareddy"
fold = os.getcwd()
print("added before :",fold)
settle = os.path.join(fold,life)
print("added after :",settle)
#makedir
try:
    money = "venkataravanalingareddy"
    well = os.getcwd()
    print(well)
    sell = os.path.join(well,money)
    os.mkdir(sell)
except FileExistsError:
    pass
#listdir
apple = os.getcwd()
terror = os.listdir(apple)
print(terror)
#remove
file = "reddymalapti"
dell = os.getcwd()
water = os.path.join(dell,file)
#os.remove(water)
