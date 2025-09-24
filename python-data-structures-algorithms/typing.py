# python is dynamically typed
# we can user tipe hints to help us if we want

name: str = "Alisson"
age: int = 29
high: float = 1.89
active: bool = True


def sum(a: int, b: int) -> int:
    return a + b

def salute(name: str) -> str: 
    return f"Hello, {name}!"

#types in a list
ages = list[int] = [2, 3, 4]
names = list[str] = ["Doo", "Didi"]

point: tuple[int, int] = (10, 20)

people = dict[str, int] = {"Alice": 30, "Bob" : 30}



