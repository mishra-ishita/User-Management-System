from db_manager import DBManager
from user import User
from exceptions import *

db = DBManager()
current_user = None

def main_menu():
    print("\n+----------------------------------+")
    print("|      📱 USER MANAGEMENT APP      |")
    print("+----------------------------------+")
    print("| 1. Login                         |")
    print("| 2. Register                      |")
    print("| 3. Logout                        |")
    print("| 4. Exit                          |")
    print("+----------------------------------+")

def user_menu(user):
    print("\n+----------------------------------+")
    print(f"| 👤 Welcome, {user['name']} |")
    print("+----------------------------------+")
    print(f"| ID       : {user['id']}")
    print(f"| Name     : {user['name']}")
    print(f"| Username : {user['username']}")
    print(f"| Address  : {user['address']}")
    print("+----------------------------------+")
    print("| 1. Change Password               |")
    print("| 2. Change Address                |")
    print("| 3. Delete My Account             |")
    print("| 4. Logout                        |")
    print("+----------------------------------+")

while True:
    try:
        if not current_user:
            main_menu()
            choice = input("Enter choice: ")

            if choice == "1":
                u = input("Username: ")
                p = input("Password: ")
                current_user = db.login(u, p)

            elif choice == "2":
                name = input("Name: ")
                username = input("Username: ")
                password = input("Password: ")
                address = input("Address: ")
                user = User(name, username, password, address)

                if not user.is_valid():
                    print("Invalid data")
                else:
                    db.register_user(user)
                    print("Registered successfully!")

            elif choice == "4":
                break

        else:
            user_menu(current_user)
            choice = input("Enter choice: ")

            if choice == "1":
                new_pass = input("New Password: ")
                db.change_password(current_user["id"], new_pass)

            elif choice == "2":
                new_addr = input("New Address: ")
                db.change_address(current_user["id"], new_addr)

            elif choice == "3":
                db.delete_user(current_user["id"])
                current_user = None
                print("Account deleted")

            elif choice == "4":
                current_user = None

    except UserError as e:
        print("Error:", e)
