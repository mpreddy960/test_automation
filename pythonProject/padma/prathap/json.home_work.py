#Check whether following json is valid or invalid. If Invalid correct it

reddy = {
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}
print(type(reddy))
#Parse the following JSON to get all the values of a key ‘name’ within an array


list_dict =[ {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },{
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }]
print(list_dict)
print(type(list_dict))
for s in list_dict:
   print("print s :",s)
   print(type(s))
   if "name" in s:
      print("it is availble")
      print("print key value", s["name"])
   else:
      print("it is not availble")


#Access the value of key2 from the following JSON
import json
using_loads = '{"klm":456,"pincode":523327,"gst":9505435}'
loads_json = json.loads(using_loads)
for c in loads_json:
   print("print c :",c)

doll = list(loads_json.keys())
print("print  doll :",type(doll))
print("print  doll :",loads_json[doll[1]])

# for v in doll:
#    print("print v  :",v)
#print("value of key2  :",loads_json["pincode"])

#PrettyPrint following JSON data
pretty_print = {"indent":"outtent","flowers":"bookes","chemistry":"bond"}
using_dumps = json.dumps(pretty_print,indent=5)
print("print pretty print  :",using_dumps)
#Sort JSON keys in and write them into a file
python_dict = {"maths":34,"physics":67,"english":78}
json_object = open("creat_file.json","w")
json_file = json.dump(python_dict,json_object,indent=5,sort_keys=json_object)
print(json_file)
#Convert the following dictionary into JSON format
python_dict = {"red":"it is a colour","tea shirt":"it is a cloth","towel":"using after bathing"}
print(type(python_dict))
convert_json_file = json.dumps(python_dict)
print("print convert json file  :",convert_json_file)
print("print type convert_json_file  :",type(convert_json_file))
