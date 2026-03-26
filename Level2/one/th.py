class User:
    def __init__(self, first_name, last_name, email, password,status='inactive'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status
def creat_user():
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    return User(first_name,last_name,email,password)
user1=creat_user()
print(user1.first_name)
v_status=input("verify your password: ")
if v_status==user1.password:
    user1.status='active'
    print(f"Your account is now active {user1.first_name}")
else:
    print(f"Your account is not active {user1.first_name} password is incorrect")
