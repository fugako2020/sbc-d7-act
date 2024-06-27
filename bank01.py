
from random import randint

# Dictionary to store accounts
accounts = {}

def main():
    balance = 0
    is_running = True

    print("Welcome to China bank ")
    username = input("Enter username: ")
    user_id = randint(0000, 9999)
    accounts[username] = {'user_id': user_id, 'balance': balance}

    while is_running:
        print("\n  China bank   ")
        print(f"Username: {username}, User ID: {user_id}")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Delete Account")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(username)
        elif choice == '2':
            deposit(username)
        elif choice == '3':
            withdraw(username)
        elif choice == '4':
            del accounts[username]
            is_running = False
        else:
            print("Invalid choice")

    print("Account Deleted")

def show_balance(username):
    balance = accounts[username]['balance']
    print(f"Hey {username}, your balance is P{balance:.2f}")

def deposit(username):
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount")
    else:
        accounts[username]['balance'] += amount
        print(f"Deposit of P{amount:.2f} successful")

def withdraw(username):
    balance = accounts[username]['balance']
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
    elif amount < 0:
        print("Amount must be greater than 0")
    else:
        accounts[username]['balance'] -= amount
        print(f"Withdrawal of P{amount:.2f} successful")

if __name__ == '__main__':
    main()
