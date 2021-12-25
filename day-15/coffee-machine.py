from main import MENU, resources

money = 0
coffee_machine_off = False

def check_resources(order_ingredients):
    """Returns True when order can be made and False when ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Return total calculated coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def make_coffee(drink_selected, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_selected}.")

def compare_cost(user_coins, drink_cost):
    """Returns True when payment accepted, False if money is insufficient"""
    if user_coins >= drink_cost:
        global money
        change = round(user_coins - drink_cost, 2)
        print(f"Here is ${change} in change.")
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

while coffee_machine_off != True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print(f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney : ${money}")
    elif user_input == "off":
        coffee_machine_off = True
    else:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            user_coins = process_coins()
            if compare_cost(user_coins, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])

