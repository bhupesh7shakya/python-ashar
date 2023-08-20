# def person(name,course):
#     print(name,course)
    
# person(course="python" ,name="bhupesh")


# task
# persons function args
# argument name parameter define
# print my name is parameter value garu

# def persons(*names):
#     for name in names:
#         print(f"my name is {name}")
        
# persons('a','b','c','d','e','f')



# args
# def person(*name):
#     print(name[0],name[1],name[2],)
    
# person('bhupesh','ram',"shyam")


# kwargs
# person()
# first,last name
# age
# descriiption about hobby
# course

# def person(**des):
#     print(f"""
#           Hello!!, My name is {des['first_name']} and
#           my last name is {des['last_name']} and
#           age is {des['age']}
#           about my self {des['desc']}
#           and hobby is{des['hobby']}
#           and i am studying {des['course']}
#           """)

# person( first_name='ram', last_name="shakya",age=12,desc = "I love coding.",hobby ="reading books ",course ='python with django')

# hello my name is <NAME> and my last name is <LAST_NAME>
# my age is <AGE>
# <HOBBY>
# i am studing <COURSE>

# def person(**kwargs):
#     # print(kwargs)
#     print(f"{kwargs['name']} studies {kwargs['course']}")
    
# person(name='ram',course="python",institue="mindrisers")