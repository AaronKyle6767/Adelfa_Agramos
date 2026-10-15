#Introduction
print("Sup im an addition and subraction calculator")
print("just gimme 2 numbers and ill do my magic")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sumtotal = 0
difference = 0

def calculate_sum():
    global sumtotal, num1, num2
    sumtotal = num1 + num2
    print(f"The sum is: {sumtotal}")

def calculate_difference():
    global difference, num1, num2
    difference = num1 - num2
    print(f"The difference is: {difference}")

calculate_sum()
calculate_difference()
