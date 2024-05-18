import data
import os


# keeps track of the machine's profit
profit = 0
# keeps track of the machiens resources
resources = data.resources

  
def clear_console():
    """
    Function that clears the console when called
    """
    # for windows
    if os.name == "nt":
        _ = os.system("cls")

    # for mac and linux (os.name is posix)
    else:
        _ = os.system("clear")



def enough_resources(order_ingredients):
    """
    Function that returns True if the coffee machine has all ingredients required to
    make the requested coffee.
    """
    # iterate over all ingredients and return False if the machine does not have 
    # enough of a certain ingredient 
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"There is not enough {item} for your order.")
            return False
    return True


def count_coints():
    """
    Function that asks the user how many coints of a certain type they want to
    insert. It then adds all the coins together and returns the total. 
    """
    print("Please insert the coins.")
    
    total = 0
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = total + quarters + dimes + nickles + pennies

    return total



def paid_enough(drink_cost, coins_sum):
    """
    Function that decides whether the coins inputted by the user are enough
    to cover the drink's cost.
    Returns True if coins_sum > drink_cost and False otherwise.
    """
    if coins_sum >= drink_cost:
        # compute the change and return it to the user
        change = round(coins_sum - drink_cost, 2)
        print(f"Here is your change: {change}")
        
        # increase the machine's profit accordingly
        global profit
        profit += drink_cost
        return True
    else:
        # compute the amount the use still has to pay
        amount_left = drink_cost - coins_sum
        print(f"Sorry that's not enough money. Please input ${amount_left}.")
        return False
    


def make_coffee(drink_name, drink_ingredients):
    """
    Function that takes the drink ingredients out of the machine's resources.
    It also prints output to the user once the coffee is prepared.
    """
    # deducting the required ingredients
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")



def give_report():
    """
    Function that gives a report of the leftover resources and profit made so far
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money made: ${profit}")



def add_resources(added_water, added_milk, added_coffee):
    """
    Function that adds ingredients to the resources dict
    """
    resources["water"] += added_water
    resources["milk"] += added_milk
    resources["coffee"] += added_coffee