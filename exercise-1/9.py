
''' Q9 : Write a program that takes the marks for 5 subjects as input and calculates the total and
average marks. '''
''' process - 1 '''
c = int(input("enter the marks in C programming :"))
calculus = int(input("enter the marks in calculus :"))
python = int(input("enter the marks in python :"))
maths = int(input("enter marks in maths :"))
ct = int(input("enter marks obtained in ct :"))
totalmarks = c + calculus + python + maths + ct
averagemarks = totalmarks / 5
print(f"total no of marks obtained = {totalmarks}")
print(f"average marks obtained = {averagemarks}")


''' process - 2 '''
def marks_calculator(n):
    marks = []
    i = 0
    while i < n:
        mark = int(input(f"Enter marks in subject {i+1}: "))
        if mark < 0 or mark > 100:
            print("Negative marks or marks greater than 100 are not allowed.")
        else:
            marks.append(mark)
            i += 1
    marks_sum = sum(marks)
    average_marks = marks_sum / n
    return f"Sum of marks = {marks_sum}\nAverage of marks = {average_marks:.2f}"
print(marks_calculator(5))