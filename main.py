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
    "money": 0.00,
}

THRESHOLD_COFFEE = 18
THRESHOLD_WATER = 50


def report():
    print(f"""
The current resources of the machine are as follows:
    water: {resources.get("water")}ml
    milk: {resources.get("milk")}ml
    coffee beans: {resources.get("coffee")}ml
    money: ${resources.get("money"):.2f}
""")


def check_resources(drink):
    low_resources = False
    for key in ["water", "milk", "coffee"]:
        if key in MENU[drink]["ingredients"]:
            if resources[key] < MENU[drink]["ingredients"][key]:
                print(f"\nSorry, there isn't enough {key}")
                low_resources = True
    if low_resources:
        return True
    else:
        return False


def process_payment(q, n, d, p):
    total = q * 0.25 + n * 0.10 + d * 0.05 + p * 0.01
    if total > MENU[coffee]["cost"]:
        remainder = total - MENU[coffee]["cost"]
        resources["money"] += MENU[coffee]["cost"]
        print(f"\nYour change is ${remainder:.2f}.")
        return True
    elif total == MENU[coffee]["cost"]:
        resources["money"] += MENU[coffee]["cost"]
        print("\nNo change.")
        return True
    else:
        print(f"\nSorry, not enough money. Your payment of ${total:.2f} will be refunded.")
        return False


def make_coffee():
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    try:
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    except TypeError and KeyError:
        pass
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    print(f"\nHere is your {coffee}. Enjoy!")


def check_resources_depletion():
    if resources["water"] < THRESHOLD_WATER or resources["coffee"] < THRESHOLD_COFFEE:
        print("\nResources depleted. Inform maintenance to refill.")
        return True


on = True

while on:

    quarters, nickels, dimes, pennies = 0, 0, 0, 0

    coffee = input("\nWhat type of coffee would you like? (espresso/latte/cappuccino): ").lower().strip()

    if coffee == "off":
        on = False
        break
    elif coffee == "report":
        report()
        continue
    elif (
        coffee != "espresso"
        and coffee != "latte"
        and coffee != "cappuccino"
        ):
        print("\nThat drink isn't available, try again")
        continue
    else:
        if check_resources(coffee):
            print("\nThe machine needs to be refilled, please select another drink or come back later.")
            continue

    print("\nPlease put the coins in")
    quarters = float(input("Quarters: ").strip() or 0)
    dimes = float(input("Dimes: ").strip() or 0)
    nickels = float(input("Nickles: ").strip() or 0)
    pennies = float(input("Pennies: ").strip() or 0)

    if process_payment(quarters, dimes, nickels, pennies):
        make_coffee()

    if check_resources_depletion():
        on = False
        break

print(f"\nReport preceding shutting down of the machine:")
report()

print("The machine is shutting down...")
