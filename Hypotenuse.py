#Imported math is required to solve for the hypotenuse
import math
#Inputs a and b
a = float(input("Enter a number for a: "))
b = float(input("Enter a number for b: "))
#Main computation
c = math.sqrt(pow(a,2)+pow(b,2))
#Final Output
print(f"The hypotenuse is: {c:.2f}")