balance = 0

while True:
    print("\nSelect an option:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    option = input("Enter the option number: ")

    if option == "1":
        print(f"Your balance is: ${balance}")
    elif option == "2":
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"You have successfully deposited ${deposit_amount}. Your new balance is ${balance}.")
        else:
            print("Deposit amount must be positive.")
    elif option == "3":
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if 0 < withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"You have successfully withdrawn ${withdraw_amount}. Your new balance is ${balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    elif option == "4":
        print("Thank you for using the bank system. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
