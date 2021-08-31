# Constructing output list WITHOUT
# Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []
# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)
print("Output List using for loop:", output_list)

#for practise
get = [input for input in input_list if input %2 ==0 ]
print("print list comphresion :",get)

# Using List comprehensions
# for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:",list_using_comp)

# Constructing output list using for loop
output_list = []
for var in range(1, 10):
    output_list.append(var ** 2)
print("Output List using for loop:", output_list)

# Constructing output list
# using list comprehension
list_using_comp = [var**2 for var in range(1, 10)]
print("Output List using list comprehension:",list_using_comp)

search = [dark**2 for dark in range(1,5)]
print("print range :",search)

input_list = [1, 2, 3, 4, 5, 6, 7]

#dictionary comprehension
output_dict = {}
# Using loop for constructing output dictionary
for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var**3

print("Output Dictionary using for loop:",output_dict)

# Given two lists containing the names of states and their
# corresponding capitals, construct a dictionary
# which maps the states with their respective capitals.
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

output_dict = {}
# Using loop for constructing output dictionary
for (key, value) in zip(state, capital):
	output_dict[key] = value
print("Output Dictionary using for loop:",output_dict)
#comprehension
cell = {gel:aloevera for (gel,aloevera) in zip(state,capital)}
print("print stae ,capitals :",cell)

#for practice
chill = {}
full = ["malapati","kalavakuntla","mulamreddy"]
off = ["prathapreddy","chandrashekar","padmareddy"]
for (names,inisials) in zip(full,off):
    chill[names] = inisials
print("print names insials :",chill)
#comprehension
voltage = {keys:values for (keys,values) in zip(full,off)}
print("print keys and values :",voltage)

#set comprehension

saw = set()
dull = [2,3,4,3]
for born in dull:
    if born %2==0:
        saw.add(born)
print("print set comprehension :",saw)
#comprehension
doal = {born for born in dull if born %2==0}
print("print even numbers in a set :",doal)


#example
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
output_set = set()
# Using loop for constructing output set
for var in input_list:
    if var % 2 == 0:
        output_set.add(var)
print("Output Set using for loop:", output_set)

#set comprehension

tool = {var for var in input_list if var %2==0}
print("print even numbers in a set  :",tool)

#for practice list comprehension
liquid = [1,2,3,45]
equal = [benz for benz in liquid if benz %2 == 0]
print("print even numbers  :",equal )
#for practice dictionarey comprehension
lock = [1,2,3,45,6]
keys = [7,8,96]
none = {key:value for (key,value) in zip(liquid,keys)}
print("print  create dictionary comprehension :",none)
#for practice set comprehension
zone = ["reddy","malapati","kamala"]
boating = {tell for tell in zone}
print("print set comprehension :",boating)
