# Python program to read
# json file
import json

# Opening JSON file
f = open("json_file.json", )

# returns JSON object as
# a dictionary
data = json.load(f)
print("print data  :",data
      )
# Iterating through the json
# list
for i in data['prathapreddy']:
	print("print i ::",i)

# Closing file
f.close()
import json

# {key:value mapping}
a = {"name": "John",
     "age": 31,
     "Salary": 25000}

# conversion to JSON done by dumps() function
b = json.dumps(a)

# printing the output
print("print b  :",type(b))
print(b)

a = '{"name": "Bob", "languages": "English"}'
# deserializes into dict
# and returns dict.
y = json.loads(a)

print("JSON string = ", y)
print(type(y))
#using dumps
import json
python_dict = {"maths":34,"english":56,"pytsics":67}
json_dict = json.dumps(python_dict)
print("print json dictionary  :",json_dict)
print(type(json_dict))
#using dump
python_dictionary = {"hights":177,"weigt":75,"width":45}
json_file = open("creat.json","w")
json_creat_file = json.dump(python_dictionary,json_file,indent=4)
print(json_creat_file)
#python file to change json file
python_dict = {"client":"reddy","gender":"male","location":"mumbai"}
convert_json_file = json.dumps(python_dict)
print("print convert to json file  :",convert_json_file)
print("print type :",type(convert_json_file))
#json file to change python file
json_file_do = '{"location":"banglore","post":"veerabhadrapuram","impotant":"location"}'
print(type(json_file_do))
conver_pytho_file = json.loads(json_file_do)
print("print python dict",conver_pytho_file)
print(type(conver_pytho_file))

detect = {
  "colors": [
    {
      "color": "black",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,255,255,1],
        "hex": "#000"
      }
    },
    {
      "color": "white",
      "category": "value",
      "code": {
        "rgba": [0,0,0,1],
        "hex": "#FFF"
      }
    },
    {
      "color": "red",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,0,0,1],
        "hex": "#FF0"
      }
    },
    {
      "color": "blue",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [0,0,255,1],
        "hex": "#00F"
      }
    },
    {
      "color": "yellow",
      "category": "hue",
      "type": "primary",
      "code": {
        "rgba": [255,255,0,1],
        "hex": "#FF0"
      }
    },
    {
      "color": "green",
      "category": "hue",
      "type": "secondary",
      "code": {
        "rgba": [0,255,0,1],
        "hex": "#0F0"
      }
    },
  ]
}

#covert  python dictionary to json file(using dumps)

print(type(detect))
fd = json.dumps(detect)
print(fd)
print(type(fd))
