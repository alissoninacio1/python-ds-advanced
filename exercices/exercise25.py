#try, catch, except
def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
    else:
        return result


division_result1 = division(10, 2)
division_result2 = division(10, 0)

division_result3 = division(10, "a")
