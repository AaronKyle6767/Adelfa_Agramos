#Introduction
print("Sup im an addition and subraction calculator")
print("just gimme 2 numbers and ill do my magic")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sumtotal = 0
difference = 0
product = 0
quotient = 0

def calculate_sum(a,b):
    global sumtotal
    sumtotal = a + b
    print("The sum is", sumtotal)

def calculate_difference(a,b):
    global difference
    difference = a - b
    print("The difference is", difference)

def calculate_product(a,b):
    global product
    product = a * b
    print("The product is", product)

def calculate_quotient(a,b):
    global quotient
    quotient = a / b
    print(f"The quotient is: {quotient:.2f}")

calculate_sum(a,b)
calculate_difference(a,b)
calculate_product(a,b)
calculate_quotient(a,b)