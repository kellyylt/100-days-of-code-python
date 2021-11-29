#Calculate tip and split among people
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
to_pay_per_person = round(bill * (1 + tip / 100) / people, 2)

print(f"Each person should pay ${to_pay_per_person}")