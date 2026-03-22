age = int(input("Enter Age: "))
health = input("Enter Health Condition (excellent/poor): ").strip().lower()
gender = input("Enter Gender (male/female): ").strip().lower()
location = input("Enter Location (city/village): ").strip().lower()
eligible = False
premium = 0
max_policy = 0
if health == "excellent" and 25 <= age <= 35:
    if location == "city" and gender == "male":
        eligible = True
        premium = 4000
        max_policy = 200000
    elif location == "city" and gender == "female":
        eligible = True
        premium = 3000
        max_policy = 200000
elif health == "poor" and 25 <= age <= 35 and location == "village" and gender == "male":
    eligible = True
    premium = 6000
    max_policy = 10000
if eligible:
    print("\nstatus: eligible for insurance.")
    print(f"monthly premium: rs. {premium}")
    print(f"maximum policy amount: rs. {max_policy}")
else:
    print("\nstatus: not eligible for insurance.")