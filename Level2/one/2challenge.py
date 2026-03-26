import time
import os 
class Management:
    users=[]
    def __init__(self,first_name,last_name,email,password,status='inactive'):
        self.firs_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status
    
    def display_user(self):
         
        print(f'First Name👤: {self.firs_name}')
        print(f'Last Name👤: {self.last_name}')
        print(f'Email📧: {self.email}')
        print(f"Status🔒: {self.status}")
        print('____________________\n')
def add_user():
    firs_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    new_user = Management(firs_name,last_name,email,password)
    Management.users.append(new_user)
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
while True:
      
    print("🎉🎉Welco to user mangement🎉🎉\n")
    time.sleep(1)
    print("1.Add user")
    print("2.Display all users")
    print("3.Exit")
    choice=input("\nChoose an action: ")
    if choice=='1':
        add_user()
        print("User added successfully🎉🎉")
        time.sleep(3)
    elif choice=='2':
       if Management.users:

        clear()
        print("Displaying all users📜...\n")
        for user in Management.users:
                user.display_user()
        time.sleep(4)
       else:
            print("No users found. Please add a user first.")
            time.sleep(2)
            
    elif choice=='3':
        print("Exiting...")
        time.sleep(2)
        break
    else:
        print("❌❌ Invalid choice❌❌")
        time.sleep(4)
        continue