class B:
    def parent(self):
        print("print reddy")

class C:
    def parent1(self):
        print("print child")

class D(B,C):
    def parent2(self):
        print("print GRAND")
p1 = D()
p1.parent()
p1.parent2()

class k:
    def doc(self):
        print("print toy")
class l:
    def box(self):
        print("print uou")
class m:
    def vb(self):
        print("print klm ")
class n:
    def cow(self):
        print("print got")
class o(k,l,n,m):
    def cv(self):
        print("print golly")
all = o()
all.cow()
all.box()
all.doc()
all.cv()
all.vb()







