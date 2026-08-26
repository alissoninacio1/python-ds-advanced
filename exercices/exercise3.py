

class Calculadora: 
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def sum(self):
        return self.num1 + self.num2 #you need to user the word 'self' here, because Python needs to know I'm searching for the value stored in the object
    

    def minus(self):
        return self.num1 - self.num2


    @staticmethod
    def multiplication(a, b):  #avoid to use self in static methods to avoid automatic reference to objetc, it works like a function but inside of the class just for organization
        return a * b 

    @staticmethod
    def division(a, b):
        return a / b



operation = Calculadora(1,2)
print(operation.sum())
print(operation.minus())
print(Calculadora.multiplication(2, 3))
print(Calculadora.division(4,2))