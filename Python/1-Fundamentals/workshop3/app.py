
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login

database = {"a":"p"}
donations = []
authorized_user = ""

while True:
  show_homepage()
  
  if authorized_user == "":
      print("You must be logged in to donate.")
  else:
      print('Logged in as ' + authorized_user)

  option = input("Choose an option:")
  
  if option == "1":
      username = input("Please enter username: ")
      password = input("Enter your password: ")

      authorized_user = login(database, username, password)
  elif option == "2":
      username = input("Please enter new username: ")
      password = input("Enter new password: ")
      
      if username in database:
          print('User already exists.')
      else:
          database[username] = password
          print('Added user')
  elif option == "3":
      if authorized_user == '':
          print('You must be logged in to donate')
      else:
          donation_string = donate(authorized_user)
          donations.append(donation_string)
  elif option == "4":
      show_donations(donations)
  elif option == "5":
      print('Goodbye')
      exit()

  else:
      print('Invalid selection')
