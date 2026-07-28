# pip install maskpass
# The standard way to securely collect a password in a terminal application is to use getpass.getpass()
# If you want the terminal to display asterisks (like ****) instead of remaining completely blank, you can use the third-party package
# pip install maskpass

from dataclasses import dataclass
import maskpass


@dataclass
class Member:
    name:str
    password:str


class MemberSystem: 

    def __init__(self):
        self.db: dict[int, Member] = {}
        self.current_id: int = 0 

    def add_user(self, name:str, password:str):
        self.current_id += 1
        self.db[self.current_id] = Member(name, password) # "In the dictionary [name], with the ID [number], add this object with name and password."


    def del_user(self, id_val:int):
        """
        # .pop() removes the key and returns its value, or None if missing
        # If the key id_val exists, it removes the key-value pair and returns the value.
        # If the key id_val does not exist, it does not crash; instead, it returns the fallback value None
        # check if something is Null and not Null: "if x is None" and "if x is not None"
        """
        if self.db.pop(id_val, None) is not None:
            print(f"User with ID {id_val} has been removed")
        else:
            print(f"ID {id_val} not found.")


    def search_user(self, partial_name:str):
        for key, val in self.db.items():
            if partial_name.lower() in val.name.lower():
                print(f"-> ID {key}: {val.name}")
            else: 
                print("User not found!")


    def update_user(self, id_val:int , new_name: str, new_password: str ):
        user = self.db.get(id_val)

        #if the user exists
        #if user: is already a valid condition in Python. It relies on truthiness—if self.db.get(id_val) finds a user object, it evaluates to True. 
        # If it finds nothing, it usually returns None, which evaluates to False
        if user:
            user.name = new_name
            user.password = new_password
            print(f"ID {id_val} updated.")
        else:
            print(f"ID {id_val} not found.")
        
            

# ==========================================
# INTERFACE DO USUÁRIO (MENU)
# ==========================================
def main():
    system = MemberSystem() #object is a class instance

    while True:
        print("\n=== SYSTEM MENU ===")
        print("1. Add | 2. Delete | 3. Search | 4. Update | 5. Exit")
        choice = input("Option: ").strip()

        match choice:
            case "1":
                name = input("Name: ")
                # maskpass.askpass mostra asteriscos (*) enquanto digita
                password = maskpass.askpass(prompt="Password: ", mask="*")
                system.add_user(name, password)
                
            case "2":
                id_val = int(input("ID to delete: "))
                system.del_user(id_val)
                
            case "3":
                partial = input("Name to search: ")
                system.search_user(partial)
                
            case "4":
                id_val = int(input("ID to update: "))
                new_name = input("New username: ")
                # Aplicado também na atualização de senha
                new_password = maskpass.askpass(prompt="New password: ", mask="*")
                system.update_user(id_val, new_name, new_password)
                
            case "5":
                print("System closed.")
                break
                
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
