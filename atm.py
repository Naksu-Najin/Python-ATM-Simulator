user_balance = 1000
user_pin = "4826"

print("Welcome to Python ATM simulator")

attempt = 3

while attempt > 0:
    correct_pin = input("Enter your PIN: ")
    
    if correct_pin == user_pin:
        print("PIN accepted!")
        break
    else:
        attempt -= 1
        print(f"Incorrect PIN. Attempts left: {attempt}")
        
    if attempt == 0:
        print("Incorrect PIN, please try again later.")
        exit()

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("-" * 50)

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print(f"Your balance is {user_balance:.2f}")
    elif choice == "2":
        try:
            amount = float(input("Enter the amount to deposit: "))
            
            if amount <= 0:
                print("Amount must be positive.")
                continue
            
            user_balance += amount
            print(f"\nYour new balance is {user_balance:.2f}")
            
        except ValueError:
            print("Please enter a valid number.")
            continue
    elif choice == "3":
        try:
            amount = float(input("Enter the amount to withdraw: "))
            
            if amount <= 0:
                print("Amount must be positive.")
                continue
            
            if amount > user_balance:
                print("Insufficient balance!")
            else:
                user_balance -= amount
                print(f"\nWithdrawn: {amount:.2f}")
                print(f"New balance: {user_balance:.2f}")
        except ValueError:
            print("Please enter a valid number.")
            continue
    
    elif choice == "4":
        print("Thank you for using python bank.")
        break
    else:
        print("Invalid choice, please try again.")
