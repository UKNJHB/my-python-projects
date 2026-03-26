import os
def clean():  
    """ وضيفة مسح الشاشة"""
    os.system("cls" if os.name=="nt"else os.system("clear"))
def buget(item,price):
    """ """
    return item*price
while True:
    clean()
    usr_budgt=float(input("Enter your spending budget: "))
    name_item=input('Enter the item you want to buy: ')
    item=int(input(f"How many {name_item}s do you want to buy? "))
    price=int(input(f"Enter the price per {name_item}: "))
    Buget=buget(item,price)
    if Buget>usr_budgt:
        print("Worring...")
    else:
        print("Success buying")
    if input("Do you want to buy another item? (y/n): ").lower()!="y":
        break