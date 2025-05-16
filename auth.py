def login():
    users = {
        "admin": "1234",
        "rescue": "1234",
        "volunteer": "1234"
    }

    print("\n🔐 Login to EDRESMS")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print(f"✅ Login successful! Welcome, {username}.")
        return username
    else:
        print("❌ Invalid credentials.")
        return 
