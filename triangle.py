print ("input the length of every side of triangle and press enter: ")

a = float (input("1st side: "))
b = float (input("2nd side: "))
c = float (input("3rd side: "))

if a<=0 or b<=0 or c<=0:
    print ("Negative number or zero is not acceptable. Please correct your numbers!")
elif a+b>c and a+c>b and b+c>a:
    print ("It is possible to draw this triangle.")
else:
    print ("It is impossible to draw this triangle.")