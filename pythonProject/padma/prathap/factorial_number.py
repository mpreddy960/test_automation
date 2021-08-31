def factorial(number):
    if number == 1:
        return number
    else:
        a = factorial(number-1)
        b = number * a
        print("print b  :",b)
        return b# return number * factorial(number-1)
print("print factorial number  :",factorial(5))

