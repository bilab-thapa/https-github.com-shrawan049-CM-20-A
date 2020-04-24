import random
print("WELCOME")

initial_balance = 400000
p = int(input("Enter you pin :"))
i = 1

while i < 2:
    print("1 - View Balance ", "2 - Withdraw Amount", "3 - Deposit", "4 - Exit")
    v = int(input("Enter your selection : "))

    if v == 1:
        print("Your balance :", initial_balance)
    
    if v == 2:
        withdraw = int (input("Enter the amount to withdraw :"))
        a = str(input("Are you Sure Y/N : "))
        if a == 'Y' or 'y':
            initial_balance = initial_balance - withdraw

    if v == 3:
        deposit = int (input("Enter the amount you want to deposit :"))
        a = str(input("Are you Sure Y/N : "))
        if a == 'Y' or 'y':
            initial_balance = initial_balance + deposit

    if v == 4:
        print("Transaction Completed")
        print("Transaction Number :", random.randint(1000,99999))
        print("Thank you for choosing us as your banking partner")
        