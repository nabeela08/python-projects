def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

num1= int(input("What is thhe first number?: "))
num2= int(input("What is thhe secomd number?: "))
for symbol in operations:
    print(symbol)
operation_symbol =input("Pick an operation from the line above: ")
calculation_func = operations[operation_symbol]
answer = calculation_func(num1,num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")
    