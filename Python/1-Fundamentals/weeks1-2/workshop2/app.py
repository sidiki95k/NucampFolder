# please park here.

from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

    name = input("Please enter your name to register:")


pin = input("Please enter your pin:")
balance = 0.0

print('name' + " has a starting balance of $" + str(balance))

while True:
    name_to_validate = input('Enter name: ')
    pin_to_validate = input('Enter PIN: ')

    if name_to_validate == 'name' and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu('name')
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout('name')
        exit()
    else:
        print('Invalid selection')

        def register_pin():
            while True:
                pin = input("Enter your 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            print("PIN successfully registered.")
        break
else:
    print("Invalid PIN. Please enter a 4-digit PIN.")
