# create a list user_list
# collection of dictionary multiple user
# username,password
# user input username ra password
# if the user name and password exits or
# user name ra paassword valid print you have been login
# successfully else invalid credentials.



USER_LIST=[

]


def login():
    username=input('Enter UserName:')
    password=input('Enter Password:')

    for user in USER_LIST:
        if username==user['username'] and password==user['password']:
            print('You have been Logged in')
            break
    else:
        print('Invalid credentials')