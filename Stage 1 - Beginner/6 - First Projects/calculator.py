to_continue = True

while to_continue:
    operator = input("Enter operation to perform: ")

    a = float(input("Enter First operand: "))
    b = float(input("Enter First second: "))
    
    if a.is_integer():
        a = int(a)
    if b.is_integer():
        b = int(b)

    match operator:
        case "+":
            print(a+b) 
        case "-":
            print(a-b) 
        case "*":
            print(a*b) 
        case "/":
            if(b == 0): raise Exception("Can not divide with zero")
            print(a/b) 
        case _:
            print("Invalid Operation")
        
    q = input("Press y/n to exit/continue : ").lower()
    if q == "y" or q == "yes":
        print("Exiting....")
        break
        
         
    

    





