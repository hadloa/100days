from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cafeMenu = Menu()
cMaker1 = CoffeeMaker()
register = MoneyMachine()

on = True

while on:
    order = input(
            'What would you like? (espresso/latte/cappuccino): ').strip().lower()

    if order == 'off':
        print('Goodbye')
        on = False
    elif order == 'report':
        cMaker1.report()
        register.report()
    else:
        order = cafeMenu.find_drink(order)
        if order:
            if cMaker1.is_resource_sufficient(order) and register.make_payment(order.cost):
                cMaker1.make_coffee(order)
