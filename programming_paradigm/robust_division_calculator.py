def safe_divide(numerator, denominator):

    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        return result
    
num1 = float(input())
num2= float(input())
result = safe_divide(num1,num2)

print(f"The result of the division is: {result}")
