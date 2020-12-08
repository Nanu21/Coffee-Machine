water_amount = 400
milk_amount = 540
coffeebeans_amount = 120
cups_amount = 9
money = 550


def quantities():
    print("The coffee machine has:\n"
          + str(water_amount) + " of water\n"
          + str(milk_amount) + " of milk\n"
          + str(coffeebeans_amount) + " of coffee beans\n"
          + str(cups_amount) + " of disposable cups\n"
          + "$" + str(money) + " of money")

def left_quantites(water_reqd, milk_reqd, coffeebeans_reqd, cost):
    global water_amount
    global milk_amount
    global coffeebeans_amount
    global money
    global cups_amount

    if water_amount < water_reqd:
        print("Sorry, not enough water!")
    else:
        water_amount -= water_reqd
        if milk_amount < milk_reqd:
            print("Sorry, not enough milk!")
        else:
            milk_amount -= milk_reqd
            if coffeebeans_amount < coffeebeans_reqd:
                print("Sorry, not enough coffee beans!")
            else:
                coffeebeans_amount -= coffeebeans_reqd
                if cups_amount < 1:
                    print("Sorry, not enough cups!")
                else:
                    cups_amount -= 1
                    money += cost
                    print("I have enough resources, making you a coffee!")


def espresso():
    water_reqd = 250
    milk_reqd = 0
    coffeebeans_reqd = 16
    cost = 4
    left_quantites(water_reqd, milk_reqd, coffeebeans_reqd, cost)


def latte():
    water_reqd = 350
    milk_reqd = 75
    coffeebeans_reqd = 20
    cost = 7
    left_quantites(water_reqd, milk_reqd, coffeebeans_reqd, cost)


def cappuccino():
    water_reqd = 200
    milk_reqd = 100
    coffeebeans_reqd = 12
    cost = 6
    left_quantites(water_reqd, milk_reqd, coffeebeans_reqd, cost)


def buy():
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    if coffee_type == "back":
        action
    elif coffee_type == "1":
        espresso()
    elif coffee_type == "2":
        latte()
    else:
        cappuccino()

def fill():
    water_added = int(input("Write how many ml of water do you want to add:"))
    milk_added = int(input("Write how many ml of milk do you want to add:"))
    coffeebeans_added = int(input("Write how many grams of coffee beans do you want to add:"))
    cups_added = int(input("Write how many disposable cups of coffee do you want to add:"))

    global water_amount
    global milk_amount
    global coffeebeans_amount
    global cups_amount
    water_amount += water_added
    milk_amount += milk_added
    coffeebeans_amount += coffeebeans_added
    cups_amount += cups_added

def take():
    global money
    print("I gave you $" + str(money))
    money = 0


while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        quantities()
    elif action == "exit":
        break

