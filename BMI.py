print ("This program will calculate your Body Mass Index (BMI).")
print ("")

w = float (input("Please enter your weight (kg): "))
h = float (input("Please enter your height (m): "))


bmi = w/h**2


if bmi < 18.5:
    print ("Your BMI is ",bmi, "and you are 'Underweight'.")
elif 18.5 <= bmi < 25:
    print ("Your BMI is ",bmi, "and you are 'Normalweight'.")
elif 25 <= bmi < 30:
    print ("Your BMI is ",bmi, "and you are 'Overweight'.")
elif 30 <= bmi < 35:
    print ("Your BMI is ",bmi, "and you are 'Obese'.")
elif 35 <= bmi < 40:
    print ("Your BMI is ",bmi, "and you are 'Extremely Obese'.")