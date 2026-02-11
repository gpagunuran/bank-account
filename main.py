
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
u1 = BankAccount(u1_name, routing_1)
u2 = BankAccount(u2_name, routing_2)

u1_savings = u1.savings_account(savings_1, 1000)
u2_savings = u2.savings_account(savings_2, 500)

u1_checking = u1.checking_account(checking_1, 2000)
u2_checking = u2.checking_account(checking_2, 0)

#Test Methods using print_info() throughout to check changes
u1.print_info()
u2.print_info()

##Savings apply interest
u1_savings.print_info()
u1_savings.apply_interest()
u1_savings.print_info()


##Savings deposit, withdraw(with minimum bal check), transfer
u1_savings.print_info()
u1_savings.deposit(500)
u1_savings.print_info()

u1_savings.withdraw(300)
u1_savings.print_info()
#min bal check -- should not take money out of balance
u2_savings.print_info()
u2_savings.withdraw(500)
u1_savings.print_info()

u1_savings.transfer(500)
u1_savings.print_info()
#check for over balance
u1_savings.transfer(1000)
u1_savings.print_info()



##Checking deposit, withdraw, transfer(with limitation)
u1_checking.print_info()
u2_checking.print_info()

u1_checking.deposit(5000)
u1_checking.print_info()

u1_checking.withdraw(300)
u1_checking.print_info()
##Check for withdrawing more than balance num
u2_checking.print_info()
u2_checking.withdraw(10)
u2_checking.print_info()

u1_checking.transfer(1000)
u1_checking.print_info()
#check for transfer limits:
u1_checking.transfer(1100)
u1_checking.print_info()



##