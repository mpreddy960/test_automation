def change(change_list,change_list1,change_list2):
    change_list[change_list1],change_list[change_list2] = change_list[change_list2],change_list[change_list1]
    return change_list
chang = [1,2,3,4,5,6,7]
chagelist1, changelist2 = 1, 4
print("after changing list :",change(chang,chagelist1,changelist2))

#swap elements in a list
# Python3 program to swap elements
# at given position
# Swap function
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))
