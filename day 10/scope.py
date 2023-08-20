# local scope
# def number():
#     x=10
#     print(x)
    
# # number()
# print(x)


# x =10
# def number():
#     print(x)
    
# # number()
# print(x)


# x =10
# def number():
#     global x
#     x=11
#     print(f"function bhitra {x}")
    
# number()
# print(f"function bahira ko {x}")

# task
# creaate is_Login varibale global variable 
# assign default value False (Boolean)
# create function name login add  2 parameter username and password
# while calling the function it takes two parameter username and password 
# if both username and password matches 
# update is_Login varibale True else  false


is_Login=False

def login(username,password):
    if username=='admin' and password == 'password':
        global is_Login
        is_Login=True
    
login('admin','passwojhgkjhrd')
print(is_Login)