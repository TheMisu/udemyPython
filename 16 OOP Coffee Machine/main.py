from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# init the coffee machine objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


# loop that runs the machine
is_on = True
while is_on:
    # access the available drinks and print them to the user
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()


    # make the machine turn off if that's what the user chose
    if choice == "off":
        print("Shutting down...")
        is_on = False
    elif choice == "report":
        # print the ingredients
        coffee_maker.report()
        print("================")
        money_machine.report()
    else:
        # search for the user's drink
        drink = menu.find_drink(choice)

        # check if the drink exists
        if drink != None:
            # check if the machine has the needed ingredients and if the user paid enough
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)