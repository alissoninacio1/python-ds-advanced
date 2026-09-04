


import os


class Register:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def show_user(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")

    #"a" - Append - will append to the end of the file
    def data_store_in_text_file(self):
        with open("user_data.txt", "a") as file:
            file.write(f"Name: {self.name}, Age: {self.age}, Email: {self.email}\n")

        with open("user_data.txt") as file:
            print(file.read())

        # remove file
        os.remove("user_data.txt")

    def perform_actions(self):
        self.show_user()
        self.data_store_in_text_file()

        

user1 = Register("Alice", 25, "alice@example.com")
user1.perform_actions()

user2 = Register("Bob", 30, "bob@example.com")
user2.perform_actions()