#Design simple calculator with basic arithmetic operations.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

while True:
     print("Select an operation to perrform:")
     print("1.ADD")
     print("2.SUBSTRACT")
     print("3.MULTIPLY")
     print("4.DIVIDE")
     print("5.Exit")


     operation = input("Enter your choice (1/2/3/4/5): ")

     if operation in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
   #code for addition
        if operation == "1":
          print("Result:", add(num1, num2))
    
    #code for sub
        elif operation == "2": 
          print("Result:", subtract(num1, num2))  
    #code for multiplication  
        elif operation == "3":
           print("Result:", multiply(num1, num2)) 
       #code for division
        elif operation =="4":
            print("Result:", divide(num1, num2)) 
        elif operation =="5" : 
            print("Exiting...")
            break   
     else:
       print("Invalid Input!Enter valid operation")   


