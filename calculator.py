import math

print ("Welcome to mak calculator.")
print ("")
print ("list of operators:")
print ("sum: +")
print ("sub: -")
print ("mul: *")
print ("div: /")
print ("sqrt: r")
print ("sin")
print ("cos")
print ("tan")
print ("cot")
print ("log")
print ("factorial: !")
print ("")

op = input("Please enter your operator: ")

if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("input first number: "))
    b = float(input("input second number: "))
elif op == "sin" or op == "cos" or op == "tan" or op == "cot":
    a = float(input("enter the angle in degree: "))*math.pi/180
elif op == "!":
    a = int(input("enter an integer number: "))
else:
    a = float(input("input a number: "))


if op == "+":
    result = a+b

elif op == "-":
    result = a-b

elif op == "*":
    result = a*b

elif op == "/":
    if b == 0:
        result = "It is undefined."
    else:
        result = a/b
elif op == "r":
    if a < 0:
        result = "It is undefined."
    else:
        result = math.sqrt(a)

elif op == "sin":
    result = math.sin(a)

elif op == "cos":
    result = math.cos(a)

elif op == "tan":
    if a == 90*math.pi/180:
        result = "It is undefined."
    else:
        result = math.tan(a)

elif op == "cot":
    if a==0:
        result = "It is undefined."
    else:
        result = 1/(math.tan(a))

elif op == "log":
    if a < 0:
        result = "It is undefined."
    else:
        result = math.log10(a)

elif op == "!":
        if a < 0:
            result = -1*(math.factorial(-a))
        else:
            result = math.factorial(a)

print (result)




