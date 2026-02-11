from BankAccount import BankAccount

class checking_account(BankAccount):

    def __init__(self, customer_name, routing_number, account_number, balance=0):
        super().__init__(self, customer_name, routing_number)
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(
            f'Added {amount} to {self.customer_name}\'s checking account. Your current balance is now(${self.current_balance})')


    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print(f"CANNOT WITHDRAW: {self.customer_name}\'s current balance (${self.balance}) is below the withdraw balance (${amount})")
        else:
            self.balance -= amount
            print(f'Successfully withdrawn ${amount} From {self.customer_name}\'s account. Your current balance is now(${self.balance})')


#transfer limitation: $1000
    def transfer(self, amount, to_account):
        #make sure you cannot transfer more than the current balance
        #transfer limitation check: no more than $1000
        #otherwise let transfer go through
        if amount > 1000:
            print(f"CANNOT TRANSFER: Transfer limit is $1000. You tried to transfer ${amount}")
            return

        if amount > self.balance:
            print(f"CANNOT TRANSFER: Insufficient funds. Balance: ${self.balance}, Transfer amount: ${amount}")
            return
        self.balance-=amount
        to_account.deposit(amount)
        print(f"Successfully transferred ${amount}. New balance: ${self.balance}")

    def print_info(self):
        print(f"{self.customer_name}'s Checking Account Balance: ${self.balance}")