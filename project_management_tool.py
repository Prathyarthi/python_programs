

def create_project():
        team_id = int(input("Enter team id : "))
        # project1 = {team_id:{'team_member1' : 12,'team_member2' : 13,'team_member3' : 14,'team_member4' : 15,'team_member5' : 16}}
        user_role['team_id'] = team_id
        

user_role = {}


admin_role = {
    'admin1':{
        'username':'pro1',
        'password' : 'pro1@123'
    },
    'admin2':{
        'username':'pro2',
        'password' : 'pro2@123'
    },
    'admin3':{
        'username':'pro3',
        'password' : 'pro3@123'
    },
}

while True:  
    # display_projects()
    role = input("Are you a user or admin? ").lower()
    if role == 'admin':
        pro = int(input("Choose which project you are accessing? "))
        if pro == 1:
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            if username == admin_role['admin1']['username']:
                if password == admin_role['admin1']['password']:
                    print("You are logged in as a admin")
                    print("1.create the project\n2.update the project\n3.view the project details\n 4.delete the project")
                    ch = int(input("enter the choice: "))
                    if ch == 1:
                        create_project()

                    
                else:
                    print("Sorry! Wrong Password")
            else:
                print("Wrong Username")
        if pro == 2:
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            if username == admin_role['admin2']['username']:
                if password == admin_role['admin2']['password']:
                    print("You are logged in as a admin")
                    print("1.create the project\n2.update the project\n3.view the project details\n4.delete the project")
                    ch = int(input("enter the choice: "))
                    break
                else:
                    print("Sorry! Wrong Password")
            else:
                print("Wrong Username")
        if pro == 3:
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            if username == admin_role['admin3']['username']:
                if password == admin_role['admin3']['password']:
                    print("You are logged in as a admin")
                    print("1.create the project\n2.update the project\n3.view the project details\n 4.delete the project")
                    ch = int(input("enter the choice: "))
                    break
                else:
                    print("Sorry! Wrong Password")
            else:
                print("Wrong Username")
    elif role == 'user':
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        team_id = int(input("Enter team id : "))
        if  user_role['team_id'] == team_id:
            print("Logged in as user")
            break

        





