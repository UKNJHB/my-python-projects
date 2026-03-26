import time

def name_email(user_name,email_user):
     if corect_email(email_user)==True:
        print(f"User '{user_name}' with email '{email_user}' sccesully addrd") 
     else:
         print(f"Invalid email format. Registered email: {email_user}")    

def corect_email(email_user):
    if "@"and"."and"com" in email_user:
        return True
    else:
        return False

user_name=input("Enter your name: ")
email_user=input("Enter your email: ")
time.sleep(3)
print('Checking user name...')
time.sleep(3)
print('Checking email...')
time.sleep(3)
name_email(user_name,email_user)