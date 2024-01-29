from utils import encrypt_rot13, load_users, save_users, find_user

def add_user():
    """Adds a new user to the password file."""
    username = input("Enter new username: ")
    if find_user(username):
        print("Cannot add. Most likely username already exists.")
        return

    real_name = input("Enter real name: ")
    password = input("Enter password: ")
    encrypted_password = encrypt_rot13(password)

    users = load_users()
    users.append([username, real_name, encrypted_password])
    save_users(users)
    print("User Created.")

if __name__ == "__main__":
    add_user()
