books={}
import os
def clean():  
    os.system("cls" if os.name=="nt"else os.system("clear"))
def addbooks():
     while True:
        clean() 
        ISBN=input("Enter ISBN: ")
        title=input("Enter title: ")
        author=input('Enter author: ')
        available=True
        books[ISBN]={"Title":title,"Author":author,"Available":available}
        print(f"Book '{title}' by {author} added to the catalog withe ISBN {ISBN}.")
        add=input("Do you want to add another book?y/n: ").lower()
        if add!="y":
            break
def Checkout():  
    while True:
         isbn=input("Enter ISBN to check out: ")
         if isbn in books:
            if books[isbn]["Available"]==True:            
               books[isbn]["Available"]=False
               book=books[isbn]["Title"]
               print(f"book '{book}' checked out successfully.")
               check_ather=input("Do you want to check out another book?(y/n): ").lower()
               if check_ather!="y":
                  break
            else:
                print("Sorry, the book is currently checked out.")
                bookCheked=input("Do you want to check out another book?(y/n): ").lower()
                if bookCheked!="y":
                  break
         elif isbn not in books:
            print("Sorry, the book is not in the list of books.")      
def  Checkin():
    while True:
          in_isbn=input("Enter ISBN to check in: ")
          if in_isbn in books:
             if books[in_isbn]["Available"]==False:            
               books[in_isbn]["Available"]=True
               book=books[in_isbn]["Title"]
               print(f"book '{book}' checked in successfully.")
               check_in=input("Do you want to check in another book?(y/n): ").lower()
               if check_in!="y":
                  break
             else:   
                print(f"The book with ISBN {in_isbn} is already available in the catalog.")
                check_in=input("Do you want to check in another book?(y/n): ").lower()
                if check_in!="y":
                   break
          else:
             print(f"Sorry,Book not found in the catalog.")
             check_in=input("Do you want to check in another book?(y/n): ").lower()
             if check_in!="y":
                    break
def Listbooks():
  while True: 
    if books:
         print("Library Catalog:")
         for ISBN in books: 
           book_info=books[ISBN]
           
           print(f"ISBN: {ISBN}, Title: {book_info['Title']}, Author: {book_info["Author"]},  Available: {book_info['Available']}")
         back=input("Do yo want to go back to the Main menu?(y/n)").lower()
         if back!='y':
            break  
    else: 
        print("The catalog is empty.")
        back=input("Do yo want to go back to the Main menu?(y/n):").lower()
        if back=='y':
            clean()
            continue
while True:
    clean()
    print("""
          Menu:
        1. Add Book
        2. Check out book
        3. Check in book
        4. List books
        5. Exit
""")
    user=input("Enter yor choice (1-5): ").strip()
    if user=="1":
        addbooks()
    elif user=="2":
        Checkout()
    elif user=="3":
        Checkin()
    elif user=="4":
        Listbooks()
    elif user=="5":
        print("Exiting the program.")  
        break
    else:
        print("Invalid choice. Please try again.")     
        continue