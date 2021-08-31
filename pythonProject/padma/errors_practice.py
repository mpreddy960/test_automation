import logging
logging.basicConfig(filename = "padma.log",
                          format = '%(asctime)s %(message)s',filemode = "w")
logs = logging.getLogger()
logs.setLevel(logging.INFO)
high = 2000
try:
    g = high/0
    print(g)
except Exception as e:
   logs.error(e)
#except ZeroDivisionError:
   # logs.error("print error",g)