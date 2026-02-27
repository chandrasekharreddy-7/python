''' Q19 : Worker efficiency is determined by time taken to complete a job. Write a program that takes
the time taken as input and prints the efficiency category. '''
time_taken = float(input("Enter the time taken to complete the job (in hours): "))
if time_taken < 2:
    print("Efficiency category: Excellent")
elif 2 <= time_taken < 4:
    print("Efficiency category: Good")
elif 4 <= time_taken < 6:
    print("Efficiency category: Average")
elif 6 <= time_taken < 8:
    print("Efficiency category: Below Average")
else:
    print("Efficiency category: Poor")


''' process - 2 '''
def efficiency_category(time_taken):
    if time_taken < 2:
        return "Efficiency category: Excellent"
    elif 2 <= time_taken < 4:
        return "Efficiency category: Good"
    elif 4 <= time_taken < 6:
        return "Efficiency category: Average"
    elif 6 <= time_taken < 8:
        return "Efficiency category: Below Average"
    else:
        return "Efficiency category: Poor"
time_taken = float(input("Enter the time taken to complete the job (in hours): "))
print(efficiency_category(time_taken))