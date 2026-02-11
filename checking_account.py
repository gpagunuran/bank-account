class checking_account(BankAccount):

    def __init__(self, customer_name, routing_number, account_number):
        super().__init__(self, customer_name, routing_number)
        self.account_number = account_number
        self.balance = 0


    def



#transfer limitation: $1000