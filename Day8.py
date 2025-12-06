#Examples of Funcions

def add(a, b):
    return a + b    
print("Addition of 5 and 3:", add(5, 3))
print(add(10, 20))

def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet("Alice"))
print(greet())

#Calculator functions

def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"       
print("\nCalculator Function Examples:")
print("5 + 3 =", calculator(5, 3, "add"))
print("10 - 4 =", calculator(10, 4, "subtract"))
print("6 * 7 =", calculator(6, 7, "multiply"))
print("20 / 5 =", calculator(20, 5, "divide"))
print("10 / 0 =", calculator(10, 0, "divide"))
print("Invalid operation:", calculator(10, 5, "modulus"))