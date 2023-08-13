class CoffeeMachine:

    def __init__(self):
        self.money = 550  # dollars

        self.water = 400  # mls
        self.milk = 540  # mls
        self.beans = 120  # grams

        self.cups = 9

    def print_state(self):  # Print current state of the machine
        print("The coffee machine has:")
        print(self.water, "ml of water")
        print(self.milk, "ml of milk")
        print(self.beans, "g of coffee beans")
        print(self.cups, "disposable cups")
        print("${} of money".format(self.money))

    def espresso(self):  # Espresso maker
        espresso_res = [self.water >= 250, self.beans >= 16, self.cups >= 1]
        print_strings = ["water", "beans", "cups"]
        if all(espresso_res):
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        else:
            for i, r in enumerate(espresso_res):
                if not r:
                    print("Sorry, not enough {}!".format(print_strings[i]))

    def latte(self):  # Latte maker
        latte_res = [self.water >= 350, self.milk >= 75, self.beans >= 20, self.cups >= 1]
        print_strings = ["water", "milk", "beans", "cups"]
        if all(latte_res):
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        else:
            for i, r in enumerate(latte_res):
                if not r:
                    print("Sorry, not enough {}!".format(print_strings[i]))

    def cappuccino(self):  # Cappuccino maker
        cappuccino_res = [self.water >= 200, self.milk >= 100, self.beans >= 12, self.cups >= 1]
        print_strings = ["water", "milk", "beans", "cups"]
        if all(cappuccino_res):
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        else:
            for i, r in enumerate(cappuccino_res):
                if not r:
                    print("Sorry, not enough {}!".format(print_strings[i]))

    def buy(self):
        n = self.inputs(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if n == "back":
            return
        elif n in ["1", "2", "3"]:
            n = int(n)
            if n == 1:
                self.espresso()
            elif n == 2:
                self.latte()
            elif n == 3:
                self.cappuccino()
            print()
        else:
            print("Invalid action")
            return

    def fill(self):
        water = int(self.inputs("Write how many ml of water you want to add:\n"))
        milk = int(self.inputs("Write how many ml of milk you want to add:\n"))
        beans = int(self.inputs("Write how many grams of coffee beans you want to add:\n"))
        cups = int(self.inputs("Write how many disposable cups you want to add:\n"))
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups
        print()

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0
        print()

    def remaining(self):
        self.print_state()
        print()

    @staticmethod
    def inputs(s):
        return input(s)

    def action(self):
        while True:
            a = self.inputs("Write action (buy, fill, take, remaining, exit):\n")
            print()
            if a == "buy":
                self.buy()
            elif a == "fill":
                self.fill()
            elif a == "take":
                self.take()
            elif a == "remaining":
                self.remaining()
            elif a == "exit":
                break
            else:
                print("Invalid Action")


def main():
    machine = CoffeeMachine()
    machine.action()


if __name__ == "__main__":
    main()
