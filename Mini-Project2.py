def show_balance(balance):
    print(f"\n💰 Your balance is: ₹{balance}\n")


def deposit_money(balance):
    try:
        amount = int(input("Enter deposit amount: "))
        if amount <= 0:
            print("❌ Amount must be positive")
            return balance
        balance += amount
        print("✅ Deposit successful")
        return balance
    except ValueError:
        print("❌ Invalid input")
        return balance


def withdraw_money(balance):
    try:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("❌ Amount must be positive")
        elif amount > balance:
            print("❌ Insufficient balance")
        else:
            balance -= amount
            print("✅ Withdrawal successful")
        return balance
    except ValueError:
        print("❌ Invalid input")
        return balance


def atm():
    balance = 5000
    print("🏦 Welcome to HDFC ATM")

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = deposit_money(balance)
        elif choice == '3':
            balance = withdraw_money(balance)
        elif choice == '4':
            print("🙏 Thank you for visiting")
            break
        else:
            print("❌ Invalid option")


atm()
