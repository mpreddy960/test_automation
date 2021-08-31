class Reddy():
    a = "welcomesssssssssssssssssss"
    def g(self,a):
        print("welcome to oops ",a)

    def h(self,a):
        print("welcome to oops hhhhhh ",a)
d = [1,2,3]

s = Reddy()
s.g(d)
s.h(d)
print("print s.a  :",s.a)
class Student:
    def check_pass_fail(self):
        if self.marks>=45:
            return True
        else:
            return False
student1 = Student()
student1.name = "prathap"
student1.marks = 86
print(student1.name)
print(student1.marks)
pass_check = student1.check_pass_fail()
print(pass_check)
student2 = Student()
student2.name = "pullareddy"
student2.marks = 34
print(student2.name)
print(student2.marks)
pass_check = student2.check_pass_fail()
print(pass_check)

#Write a Python program to import built-in array module and
# display the namespace of the said module
# import array
# for name in array.__dict__:
#     print(name)
# import array
# for n in array.__dict__:
#     print(n)


class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
for name in py_solution.__dict__:
    print(name)

#Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle():
    def b(self,max_speed,mileage):
        return max_speed,mileage
max_speed = 60
mileage = 40
d = Vehicle()
cvc = d.b(max_speed,mileage)
print("print max_speed,mileage  :",cvc)

#Create a Vehicle class without any variables and methods
class vehicle():
    pass
class felldown():
    def folden(self,sell,cell):
        return sell,cell
df = felldown()
print(df.folden("liquid","gel road"))

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()



class folder():
    felder = ["looking 55 inches led tv"]
    def __init__(self,felder):
        self.felder = felder
        print(felder)
ds = folder("tolder")
got = ds.felder


# Python3 program to
# demonstrate instantiating
# a class
class Dog:
    attr1 = "mammal"
    attr2 = "dog"
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()
#create class
class got_marks:
    lot = "mirchi"
    lot2 = "cotton"
    def cot(self):
        print(self.lot)
        print(self.lot2)
sony = got_marks()
sony.cot()



