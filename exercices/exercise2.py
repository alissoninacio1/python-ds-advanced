

def conversor(age):
    
    months = (age * 12) / 30
    days = (age * 12) % 30 + age * 365

    print(f" I lived {days} days and {months} months")



conversor(2)
