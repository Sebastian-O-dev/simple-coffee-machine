# IMPORTS
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#VARIABLES, OBJECTS etc.
my_menu = Menu()
my_coffe_maker= CoffeeMaker()
my_money_machine = MoneyMachine()
off = False

#PROCESSING LOOP
while not off:
    drink = input(f"What would you like: {my_menu.get_items()} ?: ")

    if drink == "report":
        my_coffe_maker.report()
        my_money_machine.report()
        continue
    elif drink == "off":
        off = True
        break

    coffee = my_menu.find_drink(drink)
    if not my_coffe_maker.is_resource_sufficient(coffee):
        continue

    print(f"The payment is ${coffee.cost}, please put in the coins.")

    if my_money_machine.make_payment(coffee.cost):
        my_coffe_maker.make_coffee(coffee)

#SHUTDOWN MESSAGE
print("The machine is shutting down...")