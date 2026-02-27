''' Q17 : Grading of Steel
A certain grade of steel is graded according to the following conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are assigned as follows:
• Grade 10: All three conditions are satisfied
• Grade 9: Conditions (i) and (ii) are satisfied
2

• Grade 8: Conditions (ii) and (iii) are satisfied
• Grade 7: Conditions (i) and (iii) are satisfied
• Grade 6: Only one condition is satisfied
• Grade 5: None of the conditions are satisfied
Write a program that takes as input the hardness, carbon content, and tensile strength of
the steel and prints the grade of the steel. '''
''' process - 1 '''
hardness = float(input("Enter hardness: "))
carbon = float(input("Enter carbon content: "))
tensile = float(input("Enter tensile strength: "))
c1 = hardness > 50
c2 = carbon < 0.7
c3 = tensile > 5600
if c1 and c2 and c3:
    grade = 10
elif c1 and c2:
    grade = 9
elif c2 and c3:
    grade = 8
elif c1 and c3:
    grade = 7
elif c1 or c2 or c3:
    grade = 6
else:
    grade = 5

print("Grade of steel:", grade)


''' process - 2 '''
def steel_grade(hardness, carbon, tensile):
    c1 = hardness > 50
    c2 = carbon < 0.7
    c3 = tensile > 5600
    if c1 and c2 and c3:
        grade = 10
    elif c1 and c2:
        grade = 9
    elif c2 and c3:
        grade = 8
    elif c1 and c3:
        grade = 7
    elif c1 or c2 or c3:
        grade = 6
    else:
        grade = 5
    return f"Grade of steel: {grade}"
hardness = float(input("Enter hardness: "))
carbon = float(input("Enter carbon content: "))
tensile = float(input("Enter tensile strength: "))
print(steel_grade(hardness, carbon, tensile))