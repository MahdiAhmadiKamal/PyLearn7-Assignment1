print ("This program will calculate average of grades.")
print ("")

a = float (input("math grade: "))
b = float (input("physics grade: "))
c = float (input("chemistry grade: "))

ave = (a+b+c)/3

if ave >= 17:
    print ("average: ", ave)
    print ("This student is grate.")
elif 17 > ave >= 12:
    print ("average: ", ave)
    print ("This student is normal.")
else:
   print ("average: ", ave)
   print ("This student is failed!")