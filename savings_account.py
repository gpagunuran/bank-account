from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, account_number, routing_number, balance, interest_rate=0.02):
        super().__init__(customer_name, routing_number)
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.balance = balance

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

    def deposit(self, amount):
        self.balance += amount
        print(f'Added {amount} to {self.customer_name}\'s Savings account. Your current balance is now(${self.balance})')

    def withdraw(self, amount):
        if (self.balance - amount)< 100:
            print(f"CANNOT WITHDRAW: {self.customer_name}\'s current balance (${self.balance}) would be below the minimum balance $100 after withdrawing ${amount}")
        else:
            self.balance -= amount
            print(f'Successfully withdrawn ${amount} From {self.customer_name}\'s Savings account. Your current balance is now $({self.balance})')


    def transfer(self, amount, to_account):
        #make sure you cannot transfer more than the current balance
        #transfer limitation check: no more than $1000
        #otherwise let transfer go through
        if amount > self.balance:
            print(f"CANNOT TRANSFER: Insufficient funds. {self.customer_name}'s Savings Balance: ${self.balance}, Transfer amount: ${amount}")
            return
        self.balance-=amount
        to_account.deposit(amount)
        print(f"Successfully transferred ${amount} from {self.customer_name}'s Savings Account. New balance: ${self.balance}")

    def print_info(self):
        #print the balance and interest, but not the account and routing numbers
        print(f"{self.customer_name}'s Savings Account Balance: ${self.balance}")
        print(f'Interest Rate: {self.interest_rate}\n')