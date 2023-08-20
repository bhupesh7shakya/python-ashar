while True:
    try:
        a=int(input("Enter a number number:"))
        b=int(input("Enter a second number:"))

        print(a/b)
    except ZeroDivisionError:
        print("A number can't divisible by zero number")
        
    except ValueError:
        print("Invalid Value!! It only accept integer value")
    except:
        print('Something went wrong')