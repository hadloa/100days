

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

COINS = {
    'penny': .1,
    'nickel': .5,
    'dime': .10,
    'quarter': .25
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def getAndValidateInt(prompt):
    value = 0
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("That is not a whole number. ")
        return getAndValidateInt(prompt)


while (True):

    order = 0

    while (True):
        order = input(
            'What would you like? (espresso/latte/cappuccino): ').strip().lower()
        if order in MENU or order == 'off' or order == 'report':
            break
        else:
            print("Sorry that is not on the menu!\n")
            order = 0
    if order == 'off':
        print("Goodbye!")
        break
    elif order == 'report':
        for key in resources:
            print(f'{key}: {resources[key]}')
        continue
    if MENU[order]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
    elif 'milk' in MENU[order]['ingredients'] and MENU[order]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
    elif MENU[order]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        print('Please insert coins:')
        t = getAndValidateInt("\nHow many quarters?") * COINS["quarter"]
        t += getAndValidateInt("\nHow many dimes?") * COINS["dime"]
        t += getAndValidateInt("\nHow many nickels?") * COINS["nickel"]
        t += getAndValidateInt("\nHow many pennies?") * COINS["penny"]

        if t < MENU[order]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif t > MENU[order]['cost']:
            print(f"here is your ${t - MENU[order]['cost']} change")

        print(f"here is your {order} ☕. Enjoy!")

        resources['water'] += -MENU[order]['ingredients']['water']
        if 'milk' in MENU[order]['ingredients']:
            resources['milk'] += -MENU[order]['ingredients']['milk']
        resources['coffee'] += -MENU[order]['ingredients']['coffee']
        resources['money'] += MENU[order]['cost']
