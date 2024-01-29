import string    

def encrypt_rot13(password):       #function to encrypt password  using ROT13 
    """Encrypts a password using ROT-13."""
    alphabet = string.ascii_lowercase
    rotated_alphabet = alphabet[13:] + alphabet[:13]
    table = str.maketrans(alphabet, rotated_alphabet)
    return password.translate(table)

def decrypt_rot13(encrypted_password):  #fuction to  decrypt the encrypted password  
    """Decrypts a ROT-13-encrypted password."""
    return encrypt_rot13(encrypted_password)  # ROT-13 is its own inverse

def load_users():   #this function  will be used to load user data from file 
    """Loads user information from the password file."""
    with open("passwd.txt", "r") as file:
        users = [line.strip().split(":") for line in file if line.strip()]
    return users

def save_users(users):      #this function  will update the list of users and save it back into the file
    """Saves user information to the password file."""
    with open("passwd.txt", "w") as file:
        for username, real_name, encrypted_password in users:
            file.write(f"{username}:{real_name}:{encrypted_password}\n")

def find_user(username):     #this function  will search for a specific user by his username
    """Finds a user entry by username."""
    users = load_users()
    for user in users:
        if user[0] == username:
            return user
    return None
