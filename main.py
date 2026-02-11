
from BankAccount import BankAccount
from savings_account import savings_account
from checking_account import checking_account



#Create a scenario (i.e a user opens a checking account and withdraws $x) and call proper methods to illustrate the scenario.
#Named variables for readability
u1_name = "Gabe Pagunuran"
u2_name = "Ethan Lee"
routing_1 = 101
routing_2 = 102
checking_1 = 201
checking_2 = 202
savings_1 = 301
savings_2 = 302


##Scenario: 2 Users create bank accounts, open a checking account and savings account with starting balance, withdraws into both, transfers

#Create Bank accounts, open savings and checking accounts

print("Creating Bank Accounts")
u1 = BankAccount(u1_name, routing_1)
u2 = BankAccount(u2_name, routing_2)
u1.print_info()
u2.print_info()

print("Creating Savings Accounts")
u1_savings = savings_account(u1, savings_1, 1000)
u2_savings = savings_account(u2, savings_2, 500)
u1_savings.print_info()
u2_savings.print_info()

print("Creating Checking Accounts")
u1_checking = checking_account(u1, checking_1, 2000)
u2_checking = checking_account(u2, checking_2, 0)
u1_checking.print_info()
u2_checking.print_info()

#Test Methods using print_info() throughout to check changes


##Savings apply interest
print("Test Interest")
u1_savings.print_info()
u1_savings.apply_interest()
u1_savings.print_info()


##Savings deposit, withdraw(with minimum bal check), transfer
print("Test savings deposit")
u1_savings.print_info()
u1_savings.deposit(500)
u1_savings.print_info()

print("Test savings withdraw")
u1_savings.print_info()
u1_savings.withdraw(300)
u1_savings.print_info()
#min bal check -- should not take money out of balance
u2_savings.print_info()
u2_savings.withdraw(500)
u1_savings.print_info()

print("Test savings transfer")
u1_savings.print_info()
u1_savings.transfer(500, u1_checking)
u1_savings.print_info()
#check for over balance (Should not change balance)
u1_savings.transfer(1000, u1_checking)
u1_savings.print_info()



##Checking deposit, withdraw, transfer(with limitation)

print("Test checking deposit")
u1_checking.deposit(5000)
u1_checking.print_info()

print("Test checking withdraw")
u1_checking.withdraw(300)
u1_checking.print_info()
##Check for withdrawing more than balance num
u2_checking.print_info()
u2_checking.withdraw(10)
u2_checking.print_info()

print("Test checking transfer")
u1_checking.transfer(1000)
u1_checking.print_info()
#check for transfer limits:
u1_checking.transfer(1100)
u1_checking.print_info()

##