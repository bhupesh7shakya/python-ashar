def star(func):
    def wrapper():
        print('*'*10)
        func()
        print('*'*10)
    
    return wrapper

def hastag(func):
    def wrapper():
        print('#'*10)
        func()
            
    
    return wrapper

# @hastag
# @star
def name():
    print("hello")
    
   
@star
def age():
    print("age")




hastag(star(name))()

# name()
# print()
# age()
# 
# star(name)()

# age()


# task 
#

# must use decorator

# ########
# ********
# name
# ********
# ########

# for age also

# ********
# age
# ********
