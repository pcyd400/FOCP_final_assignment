from utils import load_users, save_users, find_user

def delete_user():         #function to delete user 
    """Deletes a user from the password file."""
    username = input("Enter username: ")
    user = find_user(username)   #finding user in the file 
    if not user:
        print("User not found.")
        return

    users = load_users()
    users.remove(user)
    save_users(users)
    print("User Deleted.")

if __name__ == "__main__":
    delete_user()
