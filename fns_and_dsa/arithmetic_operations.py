def perform_operation(num1, num2, operation):
    result = 0

    while True:


        match operation:
            case "/":
                if num2 == 0:
                    print ("Cannot divided by zero.")
                    break
                else:
                    result = num1 / num2
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
        return result
    

