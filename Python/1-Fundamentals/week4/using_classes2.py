class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

user1 = User("jane", "jane@nucamp.co", "janespassword" )
print("user1.password")
user1.change_password("bestpassword")

user2 = User("sidiki", "sidiki95k@gmail.com", "sidikipassword")
print("user2.password")
user2.change_password("coolpassword")
