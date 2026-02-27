''' Q16 : Insurance Premium Calculation
A (hypothetical) insurance company wishes to automate its premium calculation and policy
restrictions. The rules are as follows:
(a) If a person's health is excellent, the person is between 25 and 35 years of age, lives
in a city, and is a male, then the premium is Rs. 4000 per month and the policy
amount cannot exceed Rs. 2 lakhs.
(b) If all the above conditions are satisfied except that the person is female, then the
premium is Rs. 3000 per month and the policy amount cannot exceed Rs. 1.5
lakhs.
(c) If a person's health is poor, the person is between 25 and 35 years of age, lives in
a village, and is a male, then the premium is Rs. 6000 per month and the policy
amount cannot exceed Rs. 1 lakh.
(d) In all other eligible cases, the premium is Rs. 5000 per month and the policy amount
cannot exceed Rs. 1.25 lakhs.
(e) A person below 25 years of age or above 65 years of age will not be insured.
(f) If the policy value requested is less than the maximum allowed, the monthly premium
amount is proportional to the policy value.
Write a program that takes necessary inputs from the user and determines whether the
person can be insured or not, and if eligible, calculates the premium amount to be paid. '''
''' process - 1 '''
age = int(input("Enter age: "))
if age < 25 or age > 65:
    print("\nPerson is NOT eligible for insurance.")
else:
    gender = input("Enter gender (male/female): ").lower()
    health = input("Enter health condition (excellent/poor): ").lower()
    location = input("Enter location (city/village): ").lower()
    policy_requested = float(input("Enter policy amount requested (in lakhs): "))
    premium = 0
    max_policy = 0
    if health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "male":
        premium = 4000
        max_policy = 2.0
    elif health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "female":
        premium = 3000
        max_policy = 1.5
    elif health == "poor" and 25 <= age <= 35 and location == "village" and gender == "male":
        premium = 6000
        max_policy = 1.0
    else:
        premium = 5000
        max_policy = 1.25
    if policy_requested > max_policy:
        print("\nRequested policy exceeds maximum allowed.")
        print("Maximum policy allowed:", max_policy, "lakhs")
    else:
        final_premium = premium * (policy_requested / max_policy)
        print("\nPerson is eligible for insurance.")
        print("Policy Amount:", policy_requested, "lakhs")
        print("Monthly Premium to be paid: Rs.",final_premium)


''' process - 2 '''
def calculate_insurance(age, gender, health, location, policy_requested):
    if age < 25 or age > 65:
        return "Person is NOT eligible for insurance."
    premium = 0
    max_policy = 0
    if health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "male":
        premium = 4000
        max_policy = 2.0
    elif health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "female":
        premium = 3000
        max_policy = 1.5
    elif health == "poor" and 25 <= age <= 35 and location == "village" and gender == "male":
        premium = 6000
        max_policy = 1.0
    else:
        premium = 5000
        max_policy = 1.25
    if policy_requested > max_policy:
        return (f"Requested policy exceeds maximum allowed.\n"
                f"Maximum policy allowed: {max_policy} lakhs")
    final_premium = premium * (policy_requested / max_policy)
    return (f"Person is eligible for insurance.\n"
            f"Policy Amount: {policy_requested} lakhs\n"
            f"Monthly Premium to be paid: Rs. {final_premium}")
age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ").lower()
health = input("Enter health condition (excellent/poor): ").lower()
location = input("Enter location (city/village): ").lower()
policy_requested = float(input("Enter policy amount requested (in lakhs): "))
result = calculate_insurance(age, gender, health, location, policy_requested)
print("\n" + result)