def show_balance(balance):
    print("Balance:", balance)
    
def deposit(balance):
    amount = float(input('Enter deposit amount: $'))
    return balance + amount

def withdraw(balance):
    amount = float(input('Enter withdrawal amount: $ '))
    return balance - amount

def logout(name):
    print("Goodbye " + name + "!")