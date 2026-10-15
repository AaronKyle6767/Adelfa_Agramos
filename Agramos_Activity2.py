#Introduction
print("Sup im an addition and subraction calculator")
print("just gimme 2 numbers and ill do my magic")
#global variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sumtotal = 0
difference = 0

def calculate_sum():
    #local variable 1
    global sumtotal, num1, num2
    sumtotal = num1 + num2
    print(f"The sum is: {sumtotal}")

def calculate_difference():
    #local variable 2
    global difference, num1, num2
    difference = num1 - num2
    print(f"The difference is: {difference}")

calculate_sum()
calculate_difference()
