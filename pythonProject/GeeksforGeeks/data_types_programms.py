
dict = {"soak":"brought","lock":"pop","full":"push"}
print(dict)
fg = {value : key for key,value in dict.items()}
print("print fg :::::",fg)



ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Reverse mapping
new_dict = {value: key for key, value in ascii_dict.items()}
print(new_dict)

import collections
list1 = [20,30,40,50,60,70,50,50,100,100,200,200,300,300,80,20,30,40]
fg= []
for item,count in collections.Counter(list1).items():
    if count > 1:
        fg.append(item)
print("print duplicates fg :::",fg)
import collections

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

duplicates = []
for item, count in collections.Counter(sample_list).items():
    if count > 1:
        duplicates.append(item)
print(duplicates)


forf = set(sample_list)
print(forf)

doc = set(list1)
print(doc)

#Filter dictionary to contain keys present in the given list

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# Filter dict using following keys
l1 = ['A', 'C', 'F']
new_dict = {key: d1[key] for key in l1}
print(new_dict)

rt = ["E","F"]
cv = {key:d1[key] for key in rt}
print(cv)


#nestead list

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# modify item
list1[1][2][2][1] = 3500
# print final result
print(list1)

# print(list1[1]) = [10, 15, [20, 25, [30, 400], 40], 45]
# print(list1[1][2]) = [20, 25, [30, 400], 40]
# print(list1[1][2][2]) = [30, 40]
# print(list1[1][2][2][1]) = 400

reddy = [52,[1, 1, [2, 2, [3,5], 4], 4], 5]
reddy[1][2][3] = 689
print(reddy)


# create a dictionary using {}
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# create a dictionary using dict()
#person = dict({"name": "Jessa", "country": "USA", "telephone": 1178})
# print(person)
# output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}
#
# create a dictionary from sequence having each item as a pair
# person = dict([("name", "Mark"), ("country", "USA"), ("telephone", 1178)])
# print(person)

# create dictionary with mixed keys keys
# first key is string and second is an integer
sample_dict = {"name": "Jessa", 10: "Mobile"}
print(sample_dict)
# output {'name': 'Jessa', 10: 'Mobile'}

# create dictionary with value as a list
person = {"name": "Jessa", "telephones": [1178, 2563, 4569]}
print(person)
# output {'name': 'Jessa', 'telephones': [1178, 2563, 4569]}

for i in person.values():
    print(i)


#Write a Python script to display the various Date Time formats.
#
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
