

import json


class Register:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def show_user_in_dict(self):
        user_dict = {
            "Name": self.name,
            "Age": self.age,
            "Email": self.email
        }
        print(user_dict)

        json_data = json.dumps(user_dict) #convert the dictionary to a JSON string
        print(json_data) #print the JSON string



        

user1 = Register("Alice", 25, "alice@example.com")
user1.show_user_in_dict()

user2 = Register("Bob", 30, "bob@example.com")
user2.show_user_in_dict()



"""
    JSO0N vs Dictionary:
    1. JSON (JavaScript Object Notation) is a lightweight data interchange format that
    is easy for humans to read and write, and easy for machines to parse and generate.
    2. A dictionary is a built-in data structure in Python that stores key-value pairs.
    3. JSON is a string representation of data, while a dictionary is an actual data structure in Python.
    4. JSON is language-independent and can be used in various programming languages, while a dictionary is specific to Python.

    5. JSON cannot be used with single quotes, while a dictionary can be used with single or double quotes.
"""
