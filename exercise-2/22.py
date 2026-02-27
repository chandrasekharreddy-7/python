''' Q22 : Write a program to convert percentage marks into grades:
• 91 - 100: S
• 81 - 90: A
• 71 - 80: B
• 61 - 70: C
• Below 60: D '''
''' process - 1 '''
marks = float(input("Enter the percentage marks: "))
if 91 <= marks <= 100:
    print("Grade: S")
elif 81 <= marks < 91:
    print("Grade: A")
elif 71 <= marks < 81:
    print("Grade: B")
elif 61 <= marks < 71:
    print("Grade: C")
elif 0 <= marks < 61:
    print("Grade: D")
else:
    print("Please enter valid percentage marks (0-100).")


''' process - 2 '''
def calculate_grade(marks):
    if 91 <= marks <= 100:
        return "Grade: S"
    elif 81 <= marks < 91:
        return "Grade: A"
    elif 71 <= marks < 81:
        return "Grade: B"
    elif 61 <= marks < 71:
        return "Grade: C"
    elif 0 <= marks < 61:
        return "Grade: D"
    else:
        return "Please enter valid percentage marks (0-100)."
marks = float(input("Enter the percentage marks: "))
print(calculate_grade(marks))