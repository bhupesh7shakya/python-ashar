# def x(a):
#     return a+10

# print(x(5))

# x=lambda a:a+10

# print(x(5))


def myFunc(n):
    return lambda x:x*n

# lambda x:x*2
myDoubler=myFunc(2)
myTripler=myFunc(3)



print(myTripler(3))
print(myTripler(4))