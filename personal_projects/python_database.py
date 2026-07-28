from dataclasses import dataclass
import getpass


#data class as in Kotlin
@dataclass
class Member:
    name: str
    password: str


db: dict[int, Member] = {}
current_ID: int = 0




#function to add users in the database
def add_usersto_db(user: Member):

    global current_ID # Fix: Declare global to modify the outer scope variable
    current_ID += 1
    db[current_ID] = user
    

def creating_user(): 
    name: str = input("Name: ")

    password: str = getpass.getpass("Password: ")
    print()

    #creating a Member object (instance)  dynamically (with parameters) and passing it directly to the function without storing it in a variable, saving both memory and code.
    add_usersto_db(Member(name, password))


def del_user(id_val: int):
    # .pop() removes the key and returns its value, or None if missing
    if (db.pop(id_val, None) is not None):
        print(f"User with ID {id_val} has been removed.")
    else:
        print(f"ID {id_val} not found")
        

def search_user():
    partial_name: str = input("Write the first name you're looking for: ")
    print()

    for key, val in db.items():
        if partial_name.lower() in val.name.lower():
            print(f"Found '{partial_name}' in {val} (ID = {key})")
           # print(val.password)


def update_user_by_id(id_val: int):
    # .get() returns None if the key does not exist
    user = db.get(id_val)
    
    if user is not None:
        # input() replaces Kotlin's print() + readln()
        user.name = input("Enter new username: ")
        user.password = input("Enter new password: ")
        print(f"User with ID {id_val} has been updated.")
    else:
        print(f"ID {id_val} not found.")



def main():
    
    print(f"Initial db {db}")
    checking: bool = True

    while(checking):
        print("Do you want to add names or not? y/n: ").strip().lower
        response: str = input()
        if response == "y": 
            creating_user()
        else:
            checking = False


    print("Searching users...")
    search_user()

    print(f"\nFinal DB: {db}")
   



if __name__ == "__main__":
    main()

# The standard way to securely collect a password in a terminal application is to use getpass.getpass()
# If you want the terminal to display asterisks (like ****) instead of remaining completely blank, you can use the third-party package
# pip install maskpass