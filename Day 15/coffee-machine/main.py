MENU = {

    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.50   
    },

    "latte":{
        "ingredients":{
            "water": 200,
            "coffee": 24,
            "milk": 150 
        },
        "cost": 2.50   
    },

    "cappuccino":{
        "ingredients":{
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0    
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def is_resource_sufficients(order_ingrediants):
    """Retuens we can fill the order with resources"""
    for item in order_ingrediants:
        if order_ingrediants[item] > resources[item]:
            print(f"Sorry ther is not enough {item}.")
            return False
    return True


def procees_coins():
    """Returns the total calculation of the coins.."""
    print("Pls insert coins.")

    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total



def is_transaction_successful(money_recevied, drink_cost):
    """Return True when the pyment is accepted, or False if money is insufficient."""
    if money_recevied >= drink_cost:
        change = round(money_recevied - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    """Remove the drink ingredients used to make it from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoye!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        report()

    else:
        #Select the drink from menu by user choice
        drink = MENU[choice]
        # call function to check ingredients available?
        if is_resource_sufficients(drink["ingredients"]):
            # taking coin from user and check for insufficient coin
            payment = procees_coins()
            # onces payment is sucessfully it will make coffee and remove resource used to make it.
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])



