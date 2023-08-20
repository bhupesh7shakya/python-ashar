user_list=[]
is_Login=False

def register(username,password):
    user={
    'username':username,
    'password':password
    }
    if is_username_exits(username):
        print("User already exits")
        return
    print(user)
    user_list.append(user)
    print("User has been Register Successfully")
    
def is_username_exits(username):
    for user in user_list:
        if user['username']==username:
            return True
    return False

def display_users():
    for user in user_list:
        print(f"{[user['username']]}|{user['password']}|")

def login(username,password):
    if  is_username_exits(username):
        for user in user_list:
            if user['username']==username and user['password']==password:
                print("Login successfully")
                global is_Login
                is_Login=True
                return True
        print("Username or password invalid")
    else:
        print("User does not exits Please reiger")
  


while True:
    choice=int(input(f"""
                Press 1 to login
                Press 2 to create an account
                Press 3 to display all the UserList
                Press 4 to exit
                """))

    if choice==1 or choice==2:
        username=input('Enter Your username:')
        password=input('Enter Your password:')

    if choice==1:
        login(username,password)
    if choice==2:
        register(username,password)
        
    if choice==3:
        if is_Login:
            display_users()
        else:
            print("Please Login First!")
        
    if choice==4:
        print('Exiting')
        break







