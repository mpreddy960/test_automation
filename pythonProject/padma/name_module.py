import os
print(os.name)

import logging

#Create and configure logger
logging.basicConfig(filename="prathap.log",
					format='%(asctime)s %(message)s',
					filemode='w')

#Creating an object
logger=logging.getLogger()
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'GFG.txt'
    f = open(filename)
    logger.info(f.read())
    text = f.read()
    f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.
except IOError:

    # print(os.error) will <class 'OSError'>
    #print('Problem reading: ' + filename)
    logger.error("reading problem",filename)

# In any case, the code then continues with
# the line after the try/except
try:
    vb = "googlejob"
    cx = open(vb,"r")
    jk = cx.read()

except IOError:
    print("print reading text file : " +vb)

try:
    zs = "reddygrop_of_chairman"
    sd = open(zs)
    sa = sd.read()
except:
    print("print problem :",zs)

hj = os.name
print(hj)
logger.info(hj)

# file open types

import os
fd = "GFG.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# # popen() provides a pipe/gateway and accesses the file directly
# file = os.popen(fd, 'w')
# file.write("Hello")
# File not closed, shown in next function.

#popen
import os
sd = "GFG.txt"
#os.rename(sd,"polution")

#path exists

import os
result = os.path.exists("file_name") #giving the name of the file as a parameter.
print(result)

file_exists = os.path.exists("reddy_malapati")
print(file_exists)

docs = os.path.getsize("file_handaling_program.py")
print(docs)

cv = os.name
print(cv)