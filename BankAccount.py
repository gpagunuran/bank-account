#BankAccount Python Class Assignment
#Made by Gabriel Pagunuran and Ethan Lee
class BankAccount:
    bank_name = "Wells Fargo"

    def __init__(self, customer_name, routing_number):
        self.customer_name = customer_name
        self.routing_number = routing_number

    def deposit(self, amount):
        self.current_balance += amount
        print(f'Added {amount} to {self.customer_name}\'s account. Your current balance is now(${self.current_balance})')

    def withdraw(self, amount):
        if (self.current_balance - amount)< self.minimum_balance:
            print(f"CANNOT WITHDRAW: {self.customer_name}\'s current balance (${self.current_balance}) is below the minimum balance (${self.minimum_balance})")
        else:
            self.current_balance -= amount
            print(f'Successfully withdrawn ${amount} From {self.customer_name}\'s account. Your current balance is now(${self.current_balance})')

    def print_info(self):
        print(f'Bank Name: {self.bank_name}')
        print(f'Customer Name: {self.customer_name}\n')
