import machine_functions
import data



# while loop that keeps the machine running
is_on = True
while is_on:
    # machine_functions.clear_console()
    choice = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

    # turn off the machine if needed
    if choice == "off":
        print("Machine turning off...")
        is_on = False
    # print the leftover resources
    elif choice == "report":
        machine_functions.give_report()
    # allow the user to add resources if they want to
    elif choice == "add":
        add_water = int(input("How much water do you want to add?: "))
        add_milk = int(input("How much milk do you want to add?: "))
        add_coffee = int(input("How much coffee do you want to add?: "))
        machine_functions.add_resources(add_water, add_milk, add_coffee)
    # make a coffee
    else:
        drink = data.MENU[choice]
        # check if the machine has enough resources
        if machine_functions.enough_resources(drink["ingredients"]):
            payment = machine_functions.count_coints()
            # if the user did not enter enough coins, ask them to add some more
            while not machine_functions.paid_enough(drink["cost"], payment):
                payment += machine_functions.count_coints()

            # otherwise prepare their coffee
            machine_functions.make_coffee(choice, drink["ingredients"]) 
    