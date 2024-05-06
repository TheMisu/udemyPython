# greeting the user
print("Welcome to the tip calculator!")

# saving the total bill
bill = float(input("How much was the total bill?\n$"))

# saving the percentage the user would like to tip
tip_percentage = int(input("How much would you like to tip?\n10%, 12% or 15%\n"))
tip_final = 1 + tip_percentage / 100

# saving how many people split the bill
people = int(input("How many people to split the bill?\n"))

# computing the price per person and rounding it to 2 decimals
individual_price = round((bill / people) * tip_final, 2)

# printing the result
print(f"Each person should pay: ${individual_price}")

