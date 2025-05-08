def login():
    print("\nLogin to continue")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "1234":
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None
