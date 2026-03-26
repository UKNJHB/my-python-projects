import time
contact={}
while True:
    print("""
    Contact Mangement

    1-Add a contact
    2-View contact
    3-Edit a contact
    4-exit
    """)
    user_inpu=int(input("lease chose a number 1-4"))
    #add
    if user_inpu==1:
        ID_user=input("Enter the contact ID: ")
        name_user=input("Pleas type a name: ")
        while True:#LOOP till enter numbes
         number_user=input("Pleas type a phone number: ")
         if number_user.isdigit():
             break
         else:
             time.sleep(2)
             print("Invalid input. Please try again.")

        contact[ID_user]={"name":name_user,"phone number":number_user}
        time.sleep(2)
        print(f"{name_user} was added successfully...")
    #view contact
    elif user_inpu==2:
        time.sleep(2)
        print(f'{contact}')
    #edit
    elif user_inpu==3:
        ID_edit= input("Pleas enter an ID edit: ")
        if ID_edit in contact:

           name_edit=input("Enter a new name: ")
           contact[ID_edit]["name"]=name_edit
           while True:
            number_edit= input("Enter a new number: ")
            if number_edit.isdigit():
                break
            else:
                print("Invalid input. Please try again.")
           contact[ID_edit]["phone number"]=number_edit
           time.sleep(2)
           print("Seccess...")
        else:
            print(f"ID {ID_edit}not found")

    #exit
    elif user_inpu==4:
        print("Exiting the program....")
        time.sleep(2)
        break
    #invalid
    else:
        time.sleep(2)
        print("Invalid input. Please try again.")