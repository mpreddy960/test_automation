# What do you mean by *args and **kwargs?
def im(*reddy):
    print(reddy)
im("life","settle","surgon","sucide",1,2,3)

def cup_of_tea(name,**adopt):
    print(name)
    print(adopt)
cup_of_tea("reddy",doc = "red",kolo = "tre")
# aplomb = aatmaviswasam
def aplomb(**adopt):
    print("print adopt :",adopt)
    for abuse in adopt:
        print(type(abuse))
        print(abuse.join("lingareddy"))
        abuse.replace("bowl","bottle")
        print(abuse)
        abuse.find("bowl")
        print("print find bowl :",abuse)
aplomb(bowl = "ball",reff ="venkatarava")


# Write a program to reverse a number in Python?
def able(k):
    b = 0
    v = 0
    while (k>0):
        b = k%10
        print("print b  :",b)
        k = int(k/10)
        print("print k  :",k)
        v = v*10+b
    return v
fg = 344
vb = able(fg)
print("print fg :",fg)
print("print vb reverse : ",vb )




# Write a Python Program to Check if a Number is a Palindrome or not?

palindrome = "121"
print("print palindrome  : ",palindrome)
its = palindrome[::-1]
if palindrome == its:
    print("print it is palindrome 121")
else:
    print("it is not palimdrome 121")

capital = "malayalam"
small = capital[::-1]
if capital == small:
    print("yes it is palindrome malayalam")
else:
    print("it is not palindrome malayalam")

folder = "20202"
bottle = folder[::-1]
if folder== bottle:
    print("print it is palindrome 20202")
else:
    print("print it is not palindrome 20202")


# Write a Python Program to Check if a Number is a Prime Number?
num = 29
flag = False
# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
# Write a Python Program to Find the Second Largest Number in a List?
second_list = [1,2,3,4,56,7]
print(second_list)
second_list.sort()
print("print second largest number in a list :",second_list[-2])


# Write a Python Program to Check Common Letters in Two Input Strings?

# How to remove an element from a list in Python
febanic = [1,2,3,4,5]
print(febanic)
febanic.remove(2)
print(febanic)

febanic.pop(3)
print(febanic)

febanic.clear()
print(febanic)


# Python Program to Print the Fibonacci sequence

# Program to print half pyramid using *
# *
# * *
# * * *
# * * * *
# * * * * *
mode = 5
for u in range(mode):
    for t in range(u+1):
        print("*",end=" ")
    print("\n")

b = 3
for g in range(b):
    for g in range(g+1):
        print("#",end="  ")
    print("\n")

# Program to print full pyramid using *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

lines = 7
for u in range(lines):
    for h in range(u+1):
        print("4",end=" ")
    print("\n")

hj = 6
for v in range(hj):
    for b in range(v+1):
        print("p",end=" ")
    print("\n")
code_line = 3
for creat in range(code_line):
    for new_t in range(creat+1):
        print("T",end="  ")
    print("\n")
import os
get = os.getcwd()
print(get)