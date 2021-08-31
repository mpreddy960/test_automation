#first method
multiply = [4,4]
all =1
for list in multiply:
   # print(list)
    all = all*list
print(all)
#second method
def multiply(listnumbers):
    list_numbers = 1
    for all_numbers in listnumbers:
        list_numbers = list_numbers * all_numbers
    return list_numbers
prathap = [2,3,4,5]
print(multiply(prathap))
#two lists multipication
def go(went):
    gone = 1
    for gang in went:
        gone = gone*gang
    return gone
speak = [2,3,5]
speak2 = [4,5,5]
print("print first list multiply :",go(speak))
print("print second list multiply  :",go(speak2))
#Reversing a List in Python
#first method
reverse_list = [6,5,4,3,2]
reverse_list.reverse()
print("print reverse list :",reverse_list)
#second  method reverse list
# Reversing a list using reverse()
def reverse(list):
    list.reverse()
    return list
list = [23,3,4,2,3,5,456,23]
print(reverse(list))
#third method
#using slicing method
list_reverse = [1,2,3,4,5,6,7,8,9]
reverse_list = list_reverse[::-1]
print("print reverse list  :",reverse_list)
#using slicing in a funtion

