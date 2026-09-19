#Import math library
import math

#Input radius
radius = float(input("Enter the radius of the garden(in meters): "))

#Area solution
area = math.pi * math.pow(radius, 2)

#Circumference solution
circumference = 2 * math.pi * radius

#Square root solution
square_root = math.sqrt(area)

#Rounded up/ Rounded down solution
rounded_down = math.floor(area)
rounded_up = math.floor(area)

#Final outputs
print(f"The area of the garden is {area:.2f} square meters")
print(f"The circumference of the garden is {circumference:.2f} meters")
print(f"The square root of the area of the garden is {square_root:.2f}")
print(f"The rounded down area of the garden is {rounded_down} square meters")
print(f"The rounded up area of the garden is {rounded_up} square meters")
