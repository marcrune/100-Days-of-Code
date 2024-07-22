from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

off = False
while not off:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        off = True
    else:
        chosen_drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(chosen_drink):
            if money_machine.make_payment(chosen_drink.cost):
                coffee_maker.make_coffee(chosen_drink)