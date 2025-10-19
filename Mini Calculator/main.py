print("......................................")
print("Welcome to the Calculator! 🧮")
print("......................................") 
history = []

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error*_* Cannot be divisible by zero."
    return x / y

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choose = input("Enter choice (1/2/3/4/5/6): ")

    if choose in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input")
            continue

        if choose == '1':
            result = add(num1, num2)
            print(result)
            history.append(f"{num1} + {num2} = {result}")
        elif choose == '2':
            result = subtract(num1, num2)
            print(result)
            history.append(f"{num1} - {num2} = {result}")
        elif choose == '3':
            result = multiply(num1, num2)
            print(result)
            history.append(f"{num1} * {num2} = {result}")
        elif choose == '4':
            result = divide(num1, num2)
            print(result)
            history.append(f"{num1} / {num2} = {result}")

    elif choose == '5':
        print("......................................")
        print("\nCalculation History:")
        print("......................................")
        if history:
            for record in history:
                print(record)
        else:
            print("No history yet *_*.")
    elif choose == '6':
        print("👋 Bye! Thanks for using the calculator.")
        break
    else:
        print("Invalid input")