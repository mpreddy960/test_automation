#first method
small_number = [3,2,2,2,3,4,5,5]
print(small_number)
small_number.sort()
print("small number in a list  :",small_number[:1])
print("small number in a list  :",small_number[0])
#second methond
small_integer = [7,5,8,4,3,9]
a = small_integer[0]
for g in small_integer:
    print("Original variable g:::", g)
    print("Original variable:::a ", a)
    if g < a:
        print("Before assigning variable g:::", g)
        print("Before assigning variable:::a ", a)
        a = g
        print("After assigning variable g:::", g)
        print("After assigning variable:::a ", a)
print("small number in a list  :",a)

