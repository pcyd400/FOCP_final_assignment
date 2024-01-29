from utils import encrypt_rot13, load_users

def login():
    """Simulates a simple login"""
    username = input("Username: ")
    password = input("Password: ")
    encrypted_password = encrypt_rot13(password)

    users = load_users()
    for user in users:
        if user[0] == username and user[2] == encrypted_password:
            print("Access granted.")
            return  # Exit the function if login is successful

    print("Access denied.")

# Call the login function to initiate the process
login()
