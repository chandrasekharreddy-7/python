''' Q18 : A library charges a fine for late returns:
• First 5 days: 50 paise
• 6-10 days: 1 rupee
• Above 10 days: 5 rupees
If returned after 30 days, membership is canceled. Write a program to display the fine or
the appropriate message. '''
''' process - 1 '''
days = int(input("Enter number of days late: "))
if days <= 5:
    fine = days * 0.50
    print("Fine to be paid: Rs.", fine)
elif days <= 10:
    fine = 5 * 0.50 + (days - 5) * 1
    print("Fine to be paid: Rs.", fine)
elif days <= 30:
    fine = 5 * 0.50 + 5 * 1 + (days - 10) * 5
    print("Fine to be paid: Rs.", fine)
else:
    print("Membership cancelled.")


''' process - 2 '''
def calculate_fine(days):
    if days <= 5:
        fine = days * 0.50
        return f"Fine to be paid: Rs. {fine}"
    elif days <= 10:
        fine = 5 * 0.50 + (days - 5) * 1
        return f"Fine to be paid: Rs. {fine}"
    elif days <= 30:
        fine = 5 * 0.50 + 5 * 1 + (days - 10) * 5
        return f"Fine to be paid: Rs. {fine}"
    else:
        return "Membership cancelled."
days = int(input("Enter number of days late: "))
print(calculate_fine(days))