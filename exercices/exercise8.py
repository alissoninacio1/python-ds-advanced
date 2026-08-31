def check_if_is_adult():
    age = int(input("Enter your age: "))

    match age:
        case age if age < 18:
            print("You are not an adult.")
        case age if age >= 18:
            print("You are an adult.")
        case age if age >= 65:
            print("You are a senior citizen.")
        case age if age < 12 and age >= 0:
            print("You are a child.")


check_if_is_adult()