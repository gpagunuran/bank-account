#BankAccount Python Class Assignment
#Made by Gabriel Pagunuran and Ethan Lee
class BankAccount:

    bank_name = "Wells Fargo"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount
        print(f'Added {amount} to {self.customer_name}\'s account. Your current balance is now(${self.current_balance})')

    def withdraw(self, amount):
        if (self.current_balance - amount)< self.minimum_balance:
            print(f"CANNOT WITHDRAW: {self.customer_name}\'s current balance (${self.current_balance}) is below the minimum balance (${self.minimum_balance})")
        else:
            self.current_balance -= amount
            print(f'Successfully withdrawn ${amount} From {self.customer_name}\'s account. Your current balance is now(${self.current_balance})')

    def print_customer_information(self):
        print(f'Bank Name: {self.bank_name}')
        print(f'Customer Name: {self.customer_name}')
        print(f'Current Balance: {self.current_balance}')
        print(f'Minimum Balance: {self.minimum_balance}\n')



p1 = BankAccount("Gabe Pagunuran", 101, 100)
p2 = BankAccount("Ethan Lee", 9, 10)

p1.print_customer_information()
p2.print_customer_information()
p1.withdraw(1)
p1.withdraw(1)
p2.withdraw(10)
p2.deposit(10)
p2.withdraw(5.25)
