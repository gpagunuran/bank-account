class SavingsAccount(BankAccount):
    def __init__(self, account_number, routing_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, routing_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest
