#If the bill was $150, split between 5 people, with 12% tip.
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, 0r 15 "))
people = int(input("How many people to split the bill "))

#Each person should pay (150 / 5) * 1.12
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people

#round the result to 2 decimal places = 33'60
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: {final_amount}")