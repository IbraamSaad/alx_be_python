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
    
    return result     


    

