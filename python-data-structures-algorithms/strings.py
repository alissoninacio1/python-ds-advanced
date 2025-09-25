"""
Inside single or double quotes (there is no char)


Slicing: 
    Specify the start index and the end index, separated by a colon.
    Get the characters from position x to position y (not included) -  [1:5]
    By leaving out the start index, the range will start at the first character - [:5]
    By leaving out the end index, the range will go to the end [5:]
    sequence[start:stop:step] - go through all the string by the step of -1


* Complete String methods in https://www.w3schools.com/python/python_strings_methods.asp

*The way to format strings is made with f-strings
    put an f in front of the string literal, and add curly brackets {}
    txt = f"My name is John, I am {age}"

*For scape chars - search in https://www.w3schools.com/python/python_strings_escape.asp


All methods are made by string.method(), if parameters are required, the parentheses are filled. 

"""


def reverse_string(word):
    return word[::-1]
print(reverse_string("Alisson"))


my_string = "inacio"
print("".join(reversed(my_string))) 




