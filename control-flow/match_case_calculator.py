num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("choose the operation (+, -, *, /): ")

match operation:
    
    case "+":
        result = num1 + num2
        print (f"The result is: {result}.")
    case "-":
        result = num1 - num2
        print (f"The result is: {num1-num2}.")
    case "*":
        result = num1 * num2
        print (f"The result is: {result}.")
    case "/":
        if operation == "/" and  num2 == 0:
            print ("Cannot divide by zero.")
        elif operation == "/" and num1 == 0:
            print ("Cannot divide by zero.")
        else:
            result = num1 / num2
            print (f"The result is: {result}.")
     
