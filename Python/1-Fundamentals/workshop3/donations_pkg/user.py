
def login(database, username, password):
    if username in database and database[username] == password:
        print('Welcome')
        return username
    elif username in database and database[username] != password:
        print("Incorrect password for " + username + ".")
        return ""
    
    else:
        print("User not found. Please register before logging in.")
        return ""