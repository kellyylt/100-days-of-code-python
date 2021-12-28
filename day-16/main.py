from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_off = False
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
drinks_menu = Menu()

while coffee_machine_off != True:
    user_input = input(f"What would you like? ({drinks_menu.get_items()}: ").lower()
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        coffee_machine_off = True
    else:
        drink = drinks_menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)