num1 = int(input ("Enter first num: "))
num2 = int(input ("Enter second num: "))
operation = input("Choose your operation (+, -, *, /): ")


if num2 == 0 and operation == "/":
    print ("Cannot divided by zero.")
else:

  match operation:
    
    case "/":
      result = num1 / num2
    case "+":
      result = num1 + num2
    case "-":
      result = num1 - num2
    case "*":
      result = num1 * num2
    
  print (f"The result is: {result}.")

    


        
    
    