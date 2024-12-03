MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money" : 10.0
}

is_on = False
if not is_on:
    on_button = input("Please type ON to turn the machine on:\n").lower()
    if on_button == "on":
        print("☺")
        is_on = True

while is_on:
    options = input("What would you like?(OPTIONS: MENU, RESOURCES, FILL, OFF)\n").lower()
    if options == "resources":
        print(f"water : {resources["water"]}\n"
              f"milk : {resources["milk"]}\n"
              f"coffee : {resources["coffee"]}\n"
              f"money : {resources["money"]}\n")
    elif options == "menu":
        print(f"\nESPRESSO: ${MENU["espresso"]["cost"]}")
        print(f"LATTE: ${MENU["latte"]["cost"]}")
        print(f"CAPPUCCINO: ${MENU["cappuccino"]["cost"]}\n")
        user_input = input("What would you like to order?\n")
        for item in MENU:
            if item == user_input:
                if (resources["water"] >= MENU[item]["ingredients"]["water"] and
                    resources["milk"] >= MENU[item]["ingredients"]["milk"] and
                    resources["coffee"] >= MENU[item]["ingredients"]["coffee"]):
                    print(f"\nPlease insert your coin, it'll be ${MENU[item]["cost"]}")
                    quarters_inserted = int(input("How many quarters?\n"))
                    dimes_inserted = int(input("How many dimes?\n"))
                    nickles_inserted = int(input("How many nickles?\n"))
                    pennies_inserted = int(input("How many pennies?\n"))
                    total_insert = ((quarters_inserted * 0.25) + (dimes_inserted * 0.10) +
                                    (nickles_inserted * 0.05) + (pennies_inserted * 0.01))
                    if total_insert < MENU[item]["cost"]:
                        print("Sorry that's not enough money. Money refunded.")
                    elif total_insert == MENU[item]["cost"]:
                        print(f"Here is your {item}. Please enjoy!")
                        resources["water"] -= MENU[item]["ingredients"]["water"]
                        resources["milk"] -= MENU[item]["ingredients"]["milk"]
                        resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
                        resources["money"] += MENU[item]["cost"]
                    else:
                        exchange = total_insert - MENU[item]["cost"]
                        after_quarter = 0
                        after_dimes = 0
                        after_nickles = 0
                        return_quarter = 0
                        return_dimes = 0
                        return_nickles = 0
                        return_pennies = 0
                        resources["water"] -= MENU[item]["ingredients"]["water"]
                        resources["milk"] -= MENU[item]["ingredients"]["milk"]
                        resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
                        resources["money"] += MENU[item]["cost"]

                        if exchange >= 0.25:
                            after_quarter = exchange % 0.25
                            return_quarter = int((exchange - after_quarter) / 0.25)
                            print(f"\n{return_quarter} quarters")
                            exchange = after_quarter
                        if exchange >= 0.10:
                            after_dimes = exchange % 0.10
                            return_dimes = int((exchange - after_dimes) / 0.10)
                            print(f"{return_dimes} dimes")
                            exchange = after_dimes
                        if exchange >= 0.05:
                            after_nickles = exchange % 0.05
                            return_nickles = int((exchange - after_nickles) / 0.05)
                            print(f"{return_nickles} nickles")
                            exchange = after_nickles
                        if exchange >= 0.01:
                            return_pennies = int(exchange / 0.01)
                            print(f"{return_pennies} pennies")
                        print("returned")
                        print(f"\nHere is your {item}. Please enjoy!☺\n")
                else:
                    print("Machine doesn't have enough resources, please fill the machine with resources")
                    print(f"water : {resources["water"]}\n"
                          f"milk : {resources["milk"]}\n"
                          f"coffee : {resources["coffee"]}\n"
                          f"money : {resources["money"]}\n")
                    pass
    elif options == "fill":
        water_fill = input("The amount of water you would like to fill?\n")
        milk_fill = input("The amount of coffee you would like to fill?\n")
        coffee_fill = input("The amount of coffee you would like to fill?\n")
        resources["water"] += int(water_fill)
        resources["milk"] += int(milk_fill)
        resources["coffee"] += int(coffee_fill)
    elif options == "off":
        is_on = False
    else:
        pass