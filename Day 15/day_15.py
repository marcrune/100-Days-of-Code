MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def return_change(total_paid, price):
    """Returns the change with 2 decimal places"""
    return format(total_paid - price, '.2f')


def check_resources(coffee_type):
    """Returns true when order can be made and false if resources are insufficient"""
    if coffee_type == 'espresso':
        if resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']:
            print('There isn\'t enough coffee.')
        elif resources['water'] < MENU[coffee_type]['ingredients']['water']:
            print('There isn\'t enough water.')
        else:
            return False
    else:
        if resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']:
            print('There isn\'t enough coffee.')
        elif resources['water'] < MENU[coffee_type]['ingredients']['water']:
            print('There isn\'t enough water.')
        elif resources['milk'] < MENU[coffee_type]['ingredients']['milk']:
            print('There isn\'t enough milk.')
        else:
            return False


def coffee_preparation(coffee_type, total, money):
    """Returns money if total (paid) is greater than or equal the coffee cost. Otherwise, it prints the total paid wasn't enough to purchase the coffee"""
    coffee_cost = MENU[coffee_type]['cost']
    if total >= coffee_cost:
        if check_resources(coffee_type) == False:
            money += coffee_cost
            if total > coffee_cost:
                print(f'Here is ${return_change(total, coffee_cost)} in change.')
            subtract_resources(coffee_type)
            print(f'Here is your {coffee_type}. Enjoy.')
    else:
        print('Sorry, that\'s not enough money. Money refunded.')
    return money


def subtract_resources(coffee_type):
    if coffee_type == 'espresso':
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']


def coffee_machine():
    off = False
    money = 0
    while not off:
        choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if choice == 'report':
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${format(money, ".2f")}')
        elif choice == 'off':
            off = True
        else:
            print('Please insert coins')
            quarters = int(input('How many quarters? '))
            dimes = int(input('How many dimes? '))
            nickles = int(input('How many nickles? '))
            pennies = int(input('How many pennies? '))
            total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
            money += coffee_preparation(choice, total, money)


coffee_machine()