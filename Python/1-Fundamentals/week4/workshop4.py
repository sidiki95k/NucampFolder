class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0.0

    def show_balance(self):
        print(self.name, 'has a balance of: $', self.balance)

    def withdraw(self, amount):

        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, recipient, amount):

        print('You are transferring', amount, 'to', recipient.name)
        entered_pin = int(input('Enter your pin:'))

        if entered_pin == self.pin:
            print('Authorized')
            print('Transferring', amount, 'to', recipient.name)

            self.balance -= amount

            recipient.balance += amount

            return True
        else:
            print('Not authorized')
            return False

    def request_money(self, sender, amount):

        print('You are requesting', amount, 'from', sender.name)
        entered_pin = int(input("Enter" + sender.name + "'s pin:"))
        entered_password = input("Enter" + self.name + "'s password:")

        if entered_pin == sender.pin and entered_password == self.password:
            print('Authorization successful.')
            print('Requesting', amount, 'from', sender.name)
            self.balance += amount
            sender.balance -= amount

            print('Request successful')
            return True
        else:
            print('Authorization failed. Please check PIN and password.')
            return False


""" Driver Code for Task 1 """
user = User("Bob", 1234, "password")
print(user.name, user.pin, user.password)

""" Driver Code for Task 2 """
user.change_name("Bobby")
user.change_pin(3456)
user.change_password("newpassword")
print(user.name, user.pin, user.password)

""" Driver Code for Task 3 """
bank_user_1 = BankUser('Bob', 1234, 'b')
bank_user_2 = BankUser('Alice', 3456, 'a')

print(
    bank_user_1.name, bank_user_1.pin,
    bank_user_1.password, bank_user_1.balance
)

""""Driver Code for Task 4 """
bank_user_1.show_balance()
bank_user_1.deposit(1000)
bank_user_1.show_balance()
bank_user_1.withdraw(500)
bank_user_1.show_balance()

# Test Task 5

bank_user_2.deposit(5000)

bank_user_2.show_balance()
bank_user_1.show_balance()

if bank_user_2.transfer_money(bank_user_1, 500):
    bank_user_2.show_balance()
    bank_user_1.show_balance()

    bank_user_2.request_money(bank_user_1, 250)

bank_user_2.show_balance()
bank_user_1.show_balance()
