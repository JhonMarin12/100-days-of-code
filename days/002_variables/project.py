print("Welcome to the tip calcualtor")

# Variables for calculation
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, ir 15? "))
num_people = int(input("How many people to split the bill? "))

# Calculation
total_bill = bill * (1 + tip/100)
bill_per_person = total_bill / num_people

# Result
print(f"Each person should pay: ${bill_per_person:.2f}")
