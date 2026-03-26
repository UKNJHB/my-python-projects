import time
import os 
class GymManagement:
    users=[]
    def __init__(self,first_name,last_name,Id,status='inactive'):
        self.first_name=first_name
        self.last_name=last_name
        self.Id=Id
        self.status=status
    def display_member(self):
         
        print(f'First Name👤: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'ID: {self.Id}')
        print(f"Status: {self.status}")
        print('____________________\n')
def add_member():
    first_name=input("Enter your first name: ").lower()
    last_name=input("Enter your last name: ").lower()
    Id=input("Enter your ID: ")
    status=input("Enter membership status (active or inactive), or click enter:").lower()
    if not status:
        status='inactive'
    new_member = GymManagement(first_name,last_name,Id,status)
    GymManagement.users.append(new_member)

def search_member():
    found = False
  

    print("1.Membership ID")
    print("2.First Name")
    print("3.Membership Status")
    choice=input('Enter your choice: ')
    if choice=='1':
        memberId=input("Enter the membership ID to search: ")
        
        for member in GymManagement.users:
             if member.Id == memberId:
                member.display_member()
                found = True
        if not found:
            print("Member not found with that ID.")
            time.sleep(2)
    elif choice=='2':
        firstname=input("Enter the first name to search: ")
       
        for member in GymManagement.users:
             if member.first_name == firstname:
                 member.display_member()
                 found = True
        if not found:
            print("Member not found with that first name.")
            time.sleep(2)
    elif choice=='3':
                memberStatus=input("Enter the membership status(active or inactive) to search: ").lower()
                
                for member in GymManagement.users:
                    if member.status == memberStatus:
                        member.display_member()
                        found = True
                if not found:
                    print("Member not found with that status.")
                    time.sleep(2)
    else:
      if not found:
        print("❌❌ Invalid choice❌❌")
  
    
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
while True:
    print("welcome to Gym Membership Management")
    time.sleep(1)
    print("Choose an action: ")
    print("1.Add new member")
    print("2.Display all members")
    print("3.Search for a member")
    print("4.Exit")
    choice=input("\nEnter your choice: ")
    if choice=='1':
        add_member()
        print("🎉Member added successfully!🎉")
        time.sleep(3)
        clear()
    elif choice=='2':
        clear()
        if GymManagement.users:
        
         print("Displaying all Members📜...\n")

         for member in GymManagement.users:
                member.display_member()
         time.sleep(5)
         clear()
        else:
         print("No members found! Please add a member first.")
         time.sleep(3)
         clear()

    elif choice=='3':
        if GymManagement.users:

          print("Searching for a member📜")
          search_member()
          time.sleep(4)
          clear()
        else:
            print("No members found! Please add a member first.")
            time.sleep(3)
            clear()

                

    elif choice=='4':
        print("Exiting...")
        time.sleep(2)
        break
    else:
        print("❌❌ Invalid choice❌❌")
        time.sleep(4)
        clear()
        continue
    