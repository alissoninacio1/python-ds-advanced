phrase: str = "Hello, World!"

print(f"this first character of the phrase is: {phrase[0]}")
print(f"this last character of the phrase is: {phrase[-1]}")

print(f"this first 5 characters of the phrase is: {phrase[:5]}")
print(f"this last 5 characters of the phrase is: {phrase[-5:]}")

print(phrase[::-1]) #reversing the phrase