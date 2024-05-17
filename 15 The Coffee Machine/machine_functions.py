import data
import os

  
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



def enough_resources(resources, order_ingredients):
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



def count_coints():
    """
    Function that asks the user how many coints of a certain type they want to
    insert. It then adds all the coins together and returns the total. 
    """
    print("Please insert the coins.")
    
    total = 0
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many quarters?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = total + quarters + dimes + nickles + pennies

    return total