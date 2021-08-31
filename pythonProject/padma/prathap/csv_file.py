import csv
with open("rk.csv","r") as xerox:
    fd = csv.reader(xerox)
    print(fd)
    for i in fd:
        print(i)
import csv
does = open("../lotr.csv","r")
coum = csv.reader(does)
for h in coum:
    print(h)

