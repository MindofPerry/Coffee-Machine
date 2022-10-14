from menu import MENU, resources
from art import logo


machine_on = True
bank = float(0)
new_order = True


def check_resources():
    """Check if the machine has enough resources to make the coffee"""
    if users_request == "espresso":
        if resources["water"] < 50 or resources["water"] == 0:
            print("Sorry, there is not enough water.")
            return "Out"
        elif resources["coffee"] < 18 or resources["coffee"] == 0:
            print("Sorry, there is not enough coffee.")
            return "Out"
    elif users_request == "latte":
        if resources["water"] < 200 or resources["water"] == 0:
            print("Sorry, there is not enough water.")
            return "Out"
        elif resources["milk"] < 150 or resources["milk"] == 0:
            print("Sorry, there is not enough milk.")
            return "Out"
        elif resources["coffee"] < 24 or resources["coffee"] == 0:
            print("Sorry, there is not enough coffee.")
            return "Out"
    elif users_request == "cappuccino":
        if resources["water"] < 250 or resources["water"] == 0:
            print("Sorry, there is not enough water.")
            return "Out"
        elif resources["milk"] < 100 or resources["milk"] == 0:
            print("Sorry, there is not enough milk.")
            return "Out"
        elif resources["coffee"] < 24 or resources["coffee"] == 0:
            print("Sorry, there is not enough coffee.")
            return "Out"


def refill_resources():
    """Ask the user if they would like to refill resources to continue using Coffee Machine when resources are low"""
    refill = input("Would you like to refill the water, milk, and coffee? Type 'Yes' or 'No': ").lower()
    if refill == "yes":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        return "Yes"
    elif refill == "no":
        return "No"


def calculate_payment():
    """Take money, Calculate change, Add funds to machine's bank"""
    global bank
    quarter_value = float(0.25)
    dime_value = float(0.10)
    nickel_value = float(0.05)
    penny_value = float(0.01)

    money_given = float(0)
    print("Please insert coins.")

    num_of_quarters = int(input("Quarters: "))
    num_of_dimes = int(input("Dimes: "))
    num_of_nickels = int(input("Nickels: "))
    num_of_pennies = int(input("Pennies: "))

    money_given += (quarter_value * num_of_quarters) + (dime_value * num_of_dimes) + \
                   (nickel_value * num_of_nickels) + (penny_value * num_of_pennies)

    if users_request == "espresso":
        if money_given < MENU["espresso"]["cost"]:
            print("Sorry that's not enough money. Money Refunded.")
        elif money_given > MENU["espresso"]["cost"]:
            change = money_given - MENU["espresso"]["cost"]
            bank += money_given - change
            print(f"Here is ${change:.2f} in change.")
            print("Here is your espresso ☕. Enjoy!")
            return True
        elif money_given == MENU["espresso"]["cost"]:
            bank += money_given
            print("Here is your espresso ☕. Enjoy!")
            return True
    elif users_request == "latte":
        if money_given < MENU["latte"]["cost"]:
            print("Sorry that's not enough money. Money Refunded.")
        elif money_given > MENU["latte"]["cost"]:
            change = money_given - MENU["latte"]["cost"]
            bank += money_given - change
            print(f"Here is ${change:.2f} in change.")
            print("Here is your latte ☕. Enjoy!")
            return True
        elif money_given == MENU["latte"]["cost"]:
            bank += money_given
            print("Here is your latte ☕. Enjoy!")
            return True
    elif users_request == "cappuccino":
        if money_given < MENU["cappuccino"]["cost"]:
            print("Sorry that's not enough money. Money Refunded.")
        elif money_given > MENU["cappuccino"]["cost"]:
            change = money_given - MENU["cappuccino"]["cost"]
            bank += money_given - change
            print(f"Here is ${change:.2f} in change.")
            print("Here is your cappuccino ☕. Enjoy!")
            return True
        elif money_given == MENU["cappuccino"]["cost"]:
            bank += money_given
            print("Here is your cappuccino ☕. Enjoy!")
            return True


def subtract_resources():
    """Subtract resources from the total resources in the machine each time a coffee is made"""
    global made_coffee
    if made_coffee:
        if users_request == "espresso":
            resources["water"] -= 50
            resources["coffee"] -= 18
        if users_request == "latte":
            resources["water"] -= 200
            resources["milk"] -= 150
            resources["coffee"] -= 24
        if users_request == "cappuccino":
            resources["water"] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 24


def report():
    """Print Report of Resources Available and Money in System"""
    global bank
    dictionary_keys = resources.keys()
    for key in dictionary_keys:
        if key == "water" or key == "milk":
            print(str(key.title()) + ": " + str(resources[key]) + "ml")
        elif key == "coffee":
            print(str(key.title()) + ": " + str(resources[key]) + "g")
    print(f"Money: ${bank:.2f}")


while machine_on:
    print(logo)
    made_coffee = False
    users_request = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
    if users_request == "espresso":
        out_of_stock = check_resources()
        if out_of_stock == "Out":
            refilling = refill_resources()
            if refilling == "Yes":
                print("Cost is $1.50")
                made_coffee = calculate_payment()
                subtract_resources()
            elif refilling == "No":
                made_coffee = False
        elif out_of_stock != "Out":
            print("Cost is $1.50")
            made_coffee = calculate_payment()
            subtract_resources()
    elif users_request == "latte":
        out_of_stock = check_resources()
        if out_of_stock == "Out":
            refilling = refill_resources()
            if refilling == "Yes":
                print("Cost is $2.50")
                made_coffee = calculate_payment()
                subtract_resources()
            elif refilling == "No":
                made_coffee = False
        elif out_of_stock != "Out":
            print("Cost is $2.50")
            made_coffee = calculate_payment()
            subtract_resources()
    elif users_request == "cappuccino":
        out_of_stock = check_resources()
        if out_of_stock == "Out":
            refilling = refill_resources()
            if refilling == "Yes":
                print("Cost is $3.00")
                made_coffee = calculate_payment()
                subtract_resources()
            elif refilling == "No":
                made_coffee = False
        elif out_of_stock != "Out":
            print("Cost is $3.00")
            made_coffee = calculate_payment()
            subtract_resources()
    elif users_request == "report":
        report()
    elif users_request == "off":
        print("Powering Down...\nGoodbye 👋")
        machine_on = False
    else:
        print("You did not provide a valid selection. Please try again.")
