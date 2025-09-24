# Python Type Casting Examples

"""
Common Casting Functions
int(): Converts compatible strings, floats (by truncating), or integers to an integer.
float(): Converts compatible strings or integers to a floating-point number.
str(): Converts other types, like numbers, into a string.
list(), tuple(), set(): Convert other iterable types into a list, tuple, or set.



GENERAL CASTING FORMULA

var_name = type_I_Want(previous_var_in_a_previous_type)

"""

# --- Casting to Integer (int) ---
print("--- Casting to Integer ---")
float_num_for_int = 10.7
str_num_for_int = "15"

# Casting a float to an int removes the decimal part (truncates)
int_from_float = int(float_num_for_int)
print(f"Float {float_num_for_int} cast to int: {int_from_float}") # Output: 10

# Casting a string containing a whole number to an int
int_from_str = int(str_num_for_int)
print(f"String '{str_num_for_int}' cast to int: {int_from_str}")   # Output: 15
print("-" * 20)


# --- Casting to Float (float) ---
print("--- Casting to Float ---")
int_num_for_float = 10
str_num_for_float = "15.5"

# Casting an integer to a float adds a decimal part
float_from_int = float(int_num_for_float)
print(f"Integer {int_num_for_float} cast to float: {float_from_int}") # Output: 10.0

# Casting a string containing a number to a float
float_from_str = float(str_num_for_float)
print(f"String '{str_num_for_float}' cast to float: {float_from_str}") # Output: 15.5
print("-" * 20)


# --- Casting to String (str) ---
print("--- Casting to String ---")
int_num_for_str = 10
float_num_for_str = 15.5

# Casting numbers to strings to concatenate them with other strings
str_from_int = "The integer is " + str(int_num_for_str)
print(str_from_int) # Output: The integer is 10

str_from_float = "The float is " + str(float_num_for_str)
print(str_from_float) # Output: The float is 15.5
print("-" * 20)


# --- Casting to Collection Types (list, tuple, set) ---
print("--- Casting to Collection Types ---")
my_tuple = (1, 2, 3, 3)
my_list = [1, 2, 2, 3, 4]

# Casting a tuple to a list
list_from_tuple = list(my_tuple)
print(f"Tuple {my_tuple} cast to list: {list_from_tuple}") # Output: [1, 2, 3, 3]

# Casting a list to a set (removes duplicates and loses order)
set_from_list = set(my_list)
print(f"List {my_list} cast to set: {set_from_list}") # Output: {1, 2, 3, 4}

# Casting a list to a tuple
tuple_from_list = tuple(my_list)
print(f"List {my_list} cast to tuple: {tuple_from_list}") # Output: (1, 2, 2, 3, 4)
print("-" * 20)


