def perform_operation(num1, num2, operation):
    result = None

    match operation:

        case "divide":
            if num2 == 0:
                result = "Cannot divided by zero"
                
            elif num2 != 0:
                result = num1 / num2
        case "add":
            result = num1 + num2
            
        case "substract":
            result = num1 - num2
            
        case "multiply":
            result = num1 * num2
    # if result is not None:
    return result     

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
    

