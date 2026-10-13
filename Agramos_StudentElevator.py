#global variables 1, 2, 3
name = input("Please enter your name: ")
score1 = int(input("Please enter your score on assessment 1: "))
score2 = int(input("Please enter your score on assessment 2: "))
score3 = int(input("Please enter your score on assessment 3: "))

#functions
def display_header():
    print("="*30)
    print("Student Performance Report".center(30))
    print("="*30)
def get_student_info():
    print(name)
    print(score1, score2, score3)
def evaluate_performance():
    #local variable 2
    average = (score1 + score2 + score3) / 3
    print(f"{average:.2f}")
    if 75 <= average <= 79:
        print("Fairly Satisfactory")
    elif 80 <= average <= 84:
        print("Satisfactory")
    elif 85 <= average <= 89:
        print("Very Satisfactory")
    elif 90 <= average <= 100:
        print("Outstanding")
    else:
        print("Failed")
def display_report():
    get_student_info()
    evaluate_performance()

#Final Output
display_header()
display_report()



