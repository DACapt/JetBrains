# Write your code here
import random
import sqlite3

class Banking:

    IIN = '400000'
    card_count = 1

    connection = sqlite3.connect('card.s3db')
    cursor = connection.cursor()
    cursor.execute('''
                    DROP TABLE IF EXISTS card;
                    ''')
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS card(
                        id INTEGER UNIQUE,
                        number TEXT UNIQUE,
                        pin TEXT,
                        balance INTEGER DEFAULT 0);
                    ''')

    connection.commit()

    def __init__(self):
        pass

    def print_database(self: object) -> None:

        self.cursor.execute("SELECT * FROM card;")
        card_table = self.cursor.fetchall()
        print(card_table)

    def create_account(self: object) -> None:

        credit_number, pin = self.gen_number_pin()

        self.cursor.execute(f'''
                            INSERT INTO card(id, number, pin, balance)
                            VALUES ({self.card_count}, {credit_number}, {pin}, {0});
                            ''')
        self.connection.commit()
        self.card_count += 1

        print("Your card has been created")
        print("Your card number: ")
        print(credit_number)
        print("Your card PIN: ")
        print(pin)

    def gen_number_pin(self):

        self.cursor.execute('''
                            SELECT number from card
                            ''')
        credit_cards = self.cursor.fetchall()

        while True:
            account_number = str(random.randint(1, 999999999)).zfill(9)
            account_identifier = self.IIN + account_number
            checksum = self.get_checksum(account_identifier)
            credit_number = account_identifier + checksum
            if credit_number not in credit_cards:
                break

        pin = str(random.randint(1, 9999)).zfill(4)

        return credit_number, pin

    @staticmethod
    def get_checksum(account_number):

        account_number_list = [int(n) for n in list(account_number)]

        sum_ = 0
        for index, number in enumerate(account_number_list):
            if not index % 2:
                number *= 2
            if number > 9:
                number -= 9
            sum_ += number

        return str(0) if not sum_ % 10 else str(10 - sum_ % 10)

    @staticmethod
    def check_card_number(account_number):
        account_number_list = [int(n) for n in list(account_number)]

        checksum = account_number_list.pop()

        sum_ = 0
        for index, number in enumerate(account_number_list):
            if not index % 2:
                number *= 2
            if number > 9:
                number -= 9
            sum_ += number

        if not (sum_ + checksum) % 10:
            return True
        else:
            return False

    def log_in(self):

        self.cursor.execute('''
                            SELECT number, pin FROM card
                            ''')
        number_pin = self.cursor.fetchall()

        print("Enter your card number: ")
        card_number = input()
        print("Enter your PIN: ")
        pin = input()

        for row in number_pin:
            print(row)
            if row[0] == card_number and row[1] == pin:
                print("You have successfully logged in!")
                self.logged_in_menu(card_number)
                break
        else:
            print("Wrong card number or PIN!")

    def logged_in_menu(self, card_number):

        def get_balance(self, card_number):

            self.cursor.execute(f'''
                                SELECT balance FROM card
                                WHERE number = {card_number}
                                ''')
            balance_list = self.cursor.fetchall()

            return balance_list[0][0]


        def print_balance(self, card_number):

            balance = get_balance(self, card_number)
            print(f"Balance: {balance}")


        def add_balance(self, card_number, income):

            balance = get_balance(self, card_number)
            self.cursor.execute(f'''
                                UPDATE card
                                SET balance = {income + balance}
                                WHERE number = {card_number} 
                                ''')
            self.connection.commit()

        def take_balance(self, card_number, income):

            balance = get_balance(self, card_number)
            self.cursor.execute(f'''
                                UPDATE card
                                SET balance = {balance - income}
                                WHERE number = {card_number} 
                                ''')
            self.connection.commit()

        def transfer_money(self, card_number):

            print("Transfer")
            print("Enter card number:")
            other_card = input()

            if not self.check_card_number(other_card):
                print("Probably you made a mistake in the card number. Please try again!")
                return 0
            elif other_card == card_number:
                print("You can't transfer money to the same account!")
                return 0

            self.cursor.execute('''
                                SELECT number from card
                                ''')
            cards = self.cursor.fetchall()
            for card in cards:
                if card[0] == other_card:
                    print("Enter how much money you want to transfer:")
                    transfer = int(input())
                    if get_balance(self, card_number) < transfer:
                        print("Not enough money")
                    else:
                        take_balance(self, card_number, transfer)
                        add_balance(self, other_card, transfer)
                        print("Success!")
                    break
            else:
                print("Such a card does not exist.")

        def close_account(self, card_number):
            self.cursor.execute(f'''
                                DELETE FROM card
                                WHERE number = {card_number}
                                ''')
            self.connection.commit()

        while True:

            print("1. Balance")
            print("2. Add income")
            print("3. Do transfer")
            print("4. Close account")
            print("5. Log out")
            print("0. Exit")

            choice = input()

            if choice == '1':
                print_balance(self, card_number)
            elif choice == '2':
                print("Enter income: ")
                income = int(input())
                add_balance(self, card_number, income)
            elif choice == '3':
                transfer_money(self, card_number)
            elif choice == '4':
                close_account(self, card_number)
                break
            elif choice == '5':
                print("Logging out!")
                break
            elif choice == '0':
                exit()

    def menu(self):

        while True:
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")

            menu_choice = input('>')

            if menu_choice == '1':
                self.create_account()
            elif menu_choice == '2':
                self.log_in()
            elif menu_choice == '0':
                print("Bye!")
                break


def main():

    banking = Banking()


    banking.menu()


main()
