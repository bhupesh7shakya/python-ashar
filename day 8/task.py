def sum(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def divide(a,b):
    print(a/b)

def multiply(a,b):
    print(a*b)
    

while True:
    operation=input("Enter the Operation +,-,/,*:")
    a=int(input("Enter the postive number"))
    b=int(input("Enter the another postive number"))
    
    if operation=="+":
        sum(a,b)
    
    elif operation =="-":
        subtract(a,b)
    # divide and multiplication garum
    
    else:
        print('Unknown Operation')
    