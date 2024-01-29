from utils import encrypt_rot13, load_users, save_users, find_user

def change_password():
    """Changes a user's password."""
    username = input("User: ")
    user = find_user(username)
    if not user:                #if user is not found in file it will  print error message.
        print("User not found.")
        return

    current_password = input("Current Password: ")
    encrypted_current_password = encrypt_rot13(current_password)  
    if encrypted_current_password != user[2]:
        print("Invalid password.")
        return

    new_password = input("New Password: ")
    confirm_password = input("Confirm: ")
    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    encrypted_new_password = encrypt_rot13(new_password)   #it will  take the new entered password and convert into ROT13 encryption format.
    user[2] = encrypted_new_password
    save_users(load_users())
    print("Password changed.")

if __name__ == "__main__":
    change_password()
