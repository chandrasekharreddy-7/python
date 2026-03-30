''' Steel Grading System: Write a program that takes hardness, carbon content, and tensile strength as input and assigns a grade:
Grade 10: All conditions met (Hardness > 50, Carbon < 0.7, Tensile > 5600).
Grade 9: Conditions (i) and (ii) are met.
Grade 6: Only one condition is met. '''
def grading_system(hardness, carbon_content, tensile_strength):
    c1 = hardness > 50
    c2 = carbon_content < 0.7
    c3 = tensile_strength > 5600
    if c1 and c2 and c3:
        return "Grade 10"
    elif c1 and c2:
        return "Grade 9"
    elif c2 and c3:
        return "Grade 8"
    elif c1 and c3:
        return "Grade 7"
    elif c1 or c2 or c3:
        return "Grade 6"
    else:
        return "Grade 5"
h = int(input("Enter hardness: "))
c = float(input("Enter carbon content: "))
t = int(input("Enter tensile strength: "))
print(f"Result: {grading_system(h, c, t)}")