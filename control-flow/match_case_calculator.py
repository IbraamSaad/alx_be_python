num1 = int(input ("Enter first num: "))
num2 = int(input ("Enter second num: "))
operation_list = ["+", "-", "*", "/"]
operation = input("Choose your operation (+, -, *, /): ")

result = int()
trails = 1
while trails > 0:

 if operation not in operation_list:
  operation = input("Choose your operation (+, -, *, /): ")
 else:
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
  trails -= 1
  print (f"The result is: {result}.")
   
  


        
    
    