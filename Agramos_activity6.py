#Activity 6
#Aaron Kyle C. Agramos
#8-Adelfa
#9/17/2026
import re #This is for number 3
#==================================================#
            #1. Payment Method Checker
#==================================================#
#Acceptable value validation
print("="*67)
valid_payment_method = ["Cash","GCash","Card"]

payment_method = input("How would you like to pay? (Cash, GCash, Card): ")
#'in' checks if the inputed payment method matches one of the three valid payment methods
if payment_method in valid_payment_method:
    print(f"Payment method is: {payment_method}")

else:
    print("Payment method is not valid.")

#==================================================#
                 #2. Grade Checker
#==================================================#
#Range validation
print("="*67)
grade = int(input("Hi, whats your grade?(1-100)"))
#only accepts numbers from 0-100, anything higher or lower will not be accepted
if 0 <= grade <= 100:
    print(f"{grade}? Thats so cool!")

else:
    print("You're capping")

#==================================================#
                #3.Student Id Checker
#==================================================#
#Pattern Validation
student_id = input("Whats ur id brochachoski?")
#pattern will now require a 4 digit number followed by a dash then another 4 digit number
pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern, student_id):
    print("aight noice")

else:
    print("FAT LIAR!!!!!")

#=================================================#
                #4. Pin Validator
#=================================================#
#Length + Content Validation
print("="*67)
pin = input("Whats your 6 digit pin?")
#checks if the pin is 6 digits and has no other data types
if len (pin) == 6 and pin.isdigit():
    print("Pin is valid")
else:
    print("Pin is not valid")

#=================================================#
            #5.Student Score Entry
#=================================================#
print("="*67)
try:
    score = int(input("Whats your score?"))

except ValueError:
    if  0 >= score >= 100:
        print("cool")
    else:
        print("NOOOOOOOOOO")
