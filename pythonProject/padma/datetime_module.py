#datetime
import datetime
v = datetime.datetime(2021,7,13,4,31,45,454)
print(v)

n = datetime.datetime.now()
print(n)

c = datetime.datetime.today()
print(c)



print("print year :",c.year)
print("print month:",c.month)
print("print date:",c.date())
print("print hour:",c.hour)
print("print minute:",c.minute)
print("print sec:",c.second)
print("print milli second :",c.microsecond)
print("print day:",c.day)
print("print days:",c.weekday())

import datetime
vel = datetime.datetime.today()
print(vel.date())
print(vel.today())
#for practice datetime
import datetime
numeric = datetime.date(2021,7,28)
print("print numeric :",numeric)
huming = datetime.datetime(2021,7,28,3,45,59,789)
print("print humming :",huming)
bolaro = datetime.datetime.today()
gang = bolaro.day
print("print day :",gang)
print("print date :",bolaro.date())
print("print  now timings",bolaro.now())
print("print minute :",bolaro.hour)
print("print seconds :",bolaro.second)
print("print ctime :",bolaro.ctime())
print("print weekday :",bolaro.weekday())
print("print  iso weekday :",bolaro.isoweekday())
print("print replace :",bolaro.replace(2001,7,28,3,59,40,678))
print("print month :",bolaro.month)
print("print time :",bolaro.time())
print("print max :",bolaro.max)
print("print isocalendar :",bolaro.isocalendar())
print("print resolution : ",bolaro.resolution)
print(bolaro.utctimetuple())
print("print timestamp :",bolaro.timestamp())
