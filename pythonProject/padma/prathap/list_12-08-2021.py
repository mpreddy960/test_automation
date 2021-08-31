#Python program to swap two elements in a list
def get(first,second,last):
    first[second],first[last] = first[last],first[second]
    return first
inter_chage = ["first","second","third","fourth","fifth","sixth"]
second,last = 0,5
change_elements = get(inter_chage,second,last)
print(change_elements)
#find largest number in  list
find_largest = [90,45,34,56,443,34,23,33,44,55,66,77]
find_largest.sort()
#print(find_largest)
print("print largest number in a list  :",find_largest[-1])
#second type
second_method = [2,3,2,32,43,424,4,3433]
largest_number = max(second_method)
print("largest using max  :",largest_number)
#find smaalest number in a list
smallest_number = [9,6,5,3,75,2,35,12,1]
smallest_number.sort()
print("print smallest number in a list  :",smallest_number[0])
print("print small number :",smallest_number[:1])
#second method
small_number = [345,346,342,341]
print("print small number min :",min(small_number))

#Python program to interchange first and last elements in a list
def swap(element):
    length = len(element)
    ele = element[0]
    element[0] = element[length-1]
    element[length-1] = ele
    return element
fisrt_last_element = ["prathapreddy","padmavathi","ramakrishnareddy"]
swap_element = swap(fisrt_last_element)
print("swap first and last element  :",swap_element)
#second method swap
def second_method(swap_element):
    swap_element[0],swap_element[-1] = swap_element[-1],swap_element[0]
    return swap_element
element_positon = ["fisrt","last","middle"]
swap_middle = second_method(element_positon)
print("print swap elements second method  :",swap_middle)
#third method
def third_method(swap_third):
    swap = swap_third[-1],swap_third[0]
    swap_third[0],swap_third[-1] = swap
    return swap_third
swap_third = ["changing element","first changing element","last changing element"]
third_way = third_method(swap_third)
print("print third method elements  :",third_way)
#Python | Ways to find length of list
list_length = [1,2,3,4,5,6,7]
print("print list  :",list_length)
added = 0
for list in list_length:
    added = added+1
    print("print added list length :",added)
#second method list length
list_find_length = ["length code","java script","java","python"]
print("print list  :",list_find_length)
print("print length :",len(list_find_length))
#third method
find_length = []
find_length.append("a")
find_length.append("b")
find_length.append("c")
find_length.append("d")
find_length.append("e")

print("print list  :",len(find_length))
#Check if element exists in list in Python
file_exists = [1,2,3,4,5,6]
print("print file exists  :",file_exists)
if 2 in file_exists:
    print("it is exists")
else:
    print("it is not exists ")
#second method
string_exists = ["strings","lists","loops","for loop"]
for exists in string_exists:
    if "strings" in exists:
        print("string is exists")
    else:
        print("string is not exists")
#third method
integer_exists = [1,2,3,4,5]
interger_find = integer_exists.count(2)
if interger_find > 0:
    print("2 intiger is exists")
else:
    print("2 intiger is not exists")

#Different ways to clear a list in Python
clear_list = [9,7,6,4,3,2]
clear_list.clear()
print("print clear list :",clear_list)
#second method
clear_list_second = [2,3,4,5,65,6]
clear_list_second*=0
print("print clear list second  :",clear_list)

