import os
gel = os.getcwd()
print(gel)
#chdir
def g():
    print(os.getcwd())
print("print beforepath")
g()
os.chdir("../")
print("print after path")
g()

# using makedirs create directorys
try:
    get = os.getcwd()
    # print(get)
    vb = get+"/high/fgfg/"
    fg = os.path.join(vb)
    df = os.makedirs(fg)
    print("created file")
except FileExistsError:
    print("alreary created directory")

#adding new folder to path
asa = "mkdir_path"
gf =os.getcwd()
settle = os.path.join(gf,asa)
print(settle)

new_path = os.path
vnvn = "new+path+line"
print("new path :",new_path)
view_path = os.getcwd()
print("view_path  :",view_path)
cv = os.path.join(view_path,vnvn)
print("print cv   :=",cv)
xc = os.mkdir(cv)
print(xc)
