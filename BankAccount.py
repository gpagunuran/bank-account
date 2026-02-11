#BankAccount Python Class Assignment
#Made by Gabriel Pagunuran and Ethan Lee
class BankAccount:
    bank_name = "Wells Fargo"

    def __init__(self, customer_name, routing_number):
        self.customer_name = customer_name
        self.routing_number = routing_number


    def print_info(self):
        print(f'Bank Name: {self.bank_name}')
        print(f'Customer Name: {self.customer_name}\n')

