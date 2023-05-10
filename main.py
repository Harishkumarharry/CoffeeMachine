from data import MENU, resources


# TODO 3: Check for resources
def check_resources(selection_ingredients):
    for ingredient in selection_ingredients:
        if selection_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True


# TODO 5: Ask for coin inserts. Calculate and show the total amount
def coin_calc():
    total = 0
    print("Please insert coins:")
    total += 0.25 * int(input("how many quarters?: "))
    total += 0.10 * int(input("how many dimes?: "))
    total += 0.05 * int(input("how many nickles?: "))
    total += 0.01 * int(input("how many pennies?: "))
    return total


# TODO 2: Create a function to process coins.
def transaction_amount(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 6: Update new resource amount.
def making_coffee(selection, selection_ingredients):
    for ingredient in selection_ingredients:
        resources[ingredient] -= selection_ingredients[ingredient]
    print(f"Here is your {selection} ☕. Enjoy")

# TODO 7: If the resource is sufficient and entered amount as well then serve the coffee.
# TODO 8: If the resource and entered amount is not sufficient return the amount and give a message


# TODO 4: Ask user there selection
is_on = True
profit = 0

while is_on:
    coffee_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_selection == "off":
        is_on = False
    elif coffee_selection == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}gm.")
        print(f"Profit: ${profit}.")
    else:
        drink = MENU[coffee_selection]
        ingredients = drink["ingredients"]
        if check_resources(ingredients):
            payment = coin_calc()
            if transaction_amount(payment, drink["cost"]):
                making_coffee(coffee_selection, ingredients)
