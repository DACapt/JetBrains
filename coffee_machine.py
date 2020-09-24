# Write your code here
class CoffeMachine():
    espresso = [250, 16, 4]
    latte = [350, 75, 20, 7]
    cappuccino = [200, 100, 12, 6]
    current_resource = [400, 540, 120, 9, 550]

    def __init__(self):
        return None
    
    def __str__(self):
        return f"A coffee machine"
        
    def __repr__(self):
        return f"An instance of CoffeMachine"
    
    def buy_espresso(self, resource):
        if resource[0] - self.espresso[0] < 0:
            print("Sorry, not enough water")
        elif resource[1] - self.espresso[1] < 0:
            print("Sorry, not enough coffee beans")
        elif resource[3] < 0:
            print("Sorry, not enough disposable cups")
        else:
            print("I have enough resources, making you a coffee!")
            resource[0] -= self.espresso[0]
            resource[2] -= self.espresso[1]
            resource[3] -= 1
            resource[4] += self.espresso[2]
        return resource


    def buy_latte_coffee(self, resource, coffee):
        if resource[0] - coffee[0] < 0:
            print("Sorry, not enough water")
        elif resource[1] - coffee[1] < 0:
            print("Sorry, not enough milk")
        elif resource[2] - coffee[2] < 0:
            print("Sorry, not enough coffee beans")
        elif resource[3] < 0:
            print("Sorry, not enough disposable cups")
        else:
            print("I have enough resources, making you a coffee!")
            resource[0] -= coffee[0]
            resource[1] -= coffee[1]
            resource[2] -= coffee[2]
            resource[3] -= 1
            resource[4] += coffee[3]
        return resource


    def buy(self, resource):
        print("What do you wanna buy? 1 - espresso, 2 - latte, 3 - cappuccino")
        buy_option = input()
        if buy_option == '1':
            return self.buy_espresso(resource)
        elif buy_option == '2':
            return self.buy_latte_coffee(resource, self.latte)
        elif buy_option == '3':
            return self.buy_latte_coffee(resource, self.cappuccino)
        elif buy_option == 'back':
            return resource
        return 0


    def fill(self, resource):
        print("Write how many ml of water do you want to add:")
        fill_water = int(input())
        print("Write how many ml of milk do you want to add:")
        fill_milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        fill_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        fill_cups = int(input())

        resource[0] += fill_water
        resource[1] += fill_milk
        resource[2] += fill_beans
        resource[3] += fill_cups

        return resource


    def take(self, resource):
        print(f"I gave you ${resource[4]}")
        resource[4] = 0
        return resource


    def display_current(self, resource):
        print("The coffee machine has:")
        print(f"{resource[0]} of water")
        print(f"{resource[1]} of milk")
        print(f"{resource[2]} of coffee beans")
        print(f"{resource[3]} of disposable cups")
        print(f"{resource[4]} of money")


    def user_input(self):
        while True:
    
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()

            if action == "buy":
                self.current_resource = self.buy(self.current_resource)
            elif action == "fill":
                self.current_resource = self.fill(self.current_resource)
            elif action == "take":
                self.current_resource = self.take(self.current_resource)
            elif action == "remaining":
                self.display_current(self.current_resource)
            elif action == "exit":
                break


coffee_machine = CoffeMachine()
coffee_machine.user_input()