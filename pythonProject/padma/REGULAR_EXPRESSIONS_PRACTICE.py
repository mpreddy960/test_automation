import re
#PRACTISE SUB METHOD
shoulder = "i dont like lazy people"
sony = re.sub("i","I",shoulder)
print(sony)
sound = re.sub("o","O",shoulder,2)
print(sound)
#PRACTISE SPLIT METHOD
folder = re.split(" ",shoulder)
print(folder)
jowl = re.split("l",shoulder)
print(jowl)
dall = re.split(" ",shoulder,1)
print(dall)
germs = re.split(" ",shoulder,2)
print(germs)
#practise search method(START,END,SPAN,STRING)
soliger = re.search("l",shoulder)
print(soliger)
print(soliger.start())
print(soliger.end())
print(soliger.span())
print(soliger.string)
#PRACTISE FINDALL
zoological = re.findall("e",shoulder)
print(zoological)
#using[]
fall = "veet tool in a PRoGRAMit is 2 in 1 soon"
sall = re.findall("[a]",fall)
print("print []    :",sall)
dall = re.findall("[tool]",fall)
print("print [WORD]    :",dall)
call = re.findall("o*",fall)
print("print 0*   :",call)
xall = re.findall("o+",fall)
print("print o+    :",xall)
zall = re.findall("\s",fall)
print("print \s   :",zall)
all = re.findall("\S",fall)
print("print \S    :",all)
fell = re.findall("\d",fall)
print("print \d    :",fell)
sell = re.findall("\D",fall)
print("print \D    :",sell)
wall = re.findall("\w",fall)
print("print \w    :",wall)
earn = re.findall("\W",fall)
print("print \W    :",earn)
hellen = re.findall("to..",fall)
print(hellen)
hell = re.findall("..to",fall)
print(hell)
gang = re.findall("t",fall)
print(gang)
kollen = re.findall("in",fall)
print("print in   :",kollen)
lop = re.findall("to",fall)
print(lop)

iol = re.findall("o{2}",fall)
print("print iol o{}  :",iol)
sudden = re.findall("[a-z]",fall)
print(sudden)

sud = re.findall("[A-Z]",fall)
print(sud)
doker = re.findall("[a-zA-Z0-9]",fall)
print(doker)
recover = re.findall("[a-z0-9]",fall)
print(recover)
#CAP SYMBOL USE IT IS RETURN TO ONLY FIRST CHARACTER

cap = re.findall("^veet",fall)
print("print cap   :",cap)
#DOLLER SYMBOL IT IS RETURN TO LAST CHARACTER

ca2doller = re.findall("soon$",fall)
print("print cap2doller   :",ca2doller)

doller = re.findall("o$",fall)
print("print doller   :",doller)

low = re.search(r"[a-z]", fall)
print("print(low)  :",low)
up = re.search(r"[A-Z]", fall)

print("print(up)  :",up)
num = re.search(r"[0-9]",fall)
print("print(num)  :",num)
fd = num.start()
print(fd)

bn = re.findall("o?",fall)
print(bn)

bone = re.findall("o$",fall)
print(bone)