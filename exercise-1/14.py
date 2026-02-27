''' Q14 : Write a program that takes a valid letter grade (S/A/B/C/D/E) as input and prints its
respective grade point (10/9/8/7/6/4). 
Note: If an invalid letter grade is entered, the program should display an appropriate message. '''
''' process - 1 '''
lettergrade = input("enter the letter grede (S/A/B/C/D/E) {to print grade point} : ")
if lettergrade == 'S':
    print("For lettergrade 'S', grade point is '10'.")
elif lettergrade == 'A':
    print("For lettergrade 'A', grade point is '9'.")
elif lettergrade == 'B':
    print("For lettergrade 'B', grade point is '8'.")
elif lettergrade == 'C':
    print("For lettergrade 'C', grade point is '7'.")
elif lettergrade == 'D':
    print("For lettergrade 'D', grade point is '6'.")
elif lettergrade == 'E':
    print("For lettergrade 'E', grade point is '4'.")
else :
    print("please enter correct letter grade.")


''' process - 2 '''
def grade_point(lettergrade):
    if lettergrade == 'S':
        return "For letter grade 'S', grade point is '10'."
    elif lettergrade == 'A':
        return "For letter grade 'A', grade point is '9'."
    elif lettergrade == 'B':
        return "For letter grade 'B', grade point is '8'."
    elif lettergrade == 'C':
        return "For letter grade 'C', grade point is '7'."
    elif lettergrade == 'D':
        return "For letter grade 'D', grade point is '6'."
    elif lettergrade == 'E':
        return "For letter grade 'E', grade point is '4'."
    else:
        return "Please enter correct letter grade."
lettergrade = input("Enter the letter grade (S/A/B/C/D/E): ").upper()
print(grade_point(lettergrade))