def calculator():
    print("simple Calculator using Python")
    print("Available operations: +, -, *, /")
    
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!"
    else:
        result = "Invalid operator!"
        
    print("Result:", result)

    while True:
        calculator()
        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("goodbye! ")
            break
