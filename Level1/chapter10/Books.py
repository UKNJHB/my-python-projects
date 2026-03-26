import os
def clean():  
    os.system("cls" if os.name=="nt"else os.system("clear"))
def Menu():
    print("""
          Menu:
        1. Add Book
        2. Check out book
        3. Check in book
        4. List books
        5. Exit
""")
books={}
while True:    
    Menu()
    user=input("Enter yor choice (1-5): ").strip()
    if user=="1":
      while True: 
        ISBN=input("Enter ISBN: ")
        title=input("Enter title: ")
        author=input('Enter author: ')
        available=True
        books[ISBN]={"Title":title,"Author":author,"Available":available}
        print(f"Book '{title}' by {author} added to the catalog withe ISBN {ISBN}.")
        add=input("Do you want to add another book?y/n: ").lower()
        if add=="y":
           clean()
           continue
        else:
           clean()
           break
    elif user=="2":
       while True:
         isbn=input("Enter ISBN to check out: ")
         if isbn in books:
            if books[isbn]["Available"]==True:            
               books[isbn]["Available"]=False
               book=books[isbn]["Title"]
               print(f"book '{book}' checked out successfully.")
               check_ather=input("Do you want to check out another book?(y/n): ").lower()
               if check_ather=="y":
                  clean()
                  continue
               else:
                    clean()
                    break
            else:
                print("Sorry, the book is currently checked out.")
                bookCheked=input("Do you want to check out another book?(y/n): ").lower()
                if bookCheked=="y":
                  clean()                 
                  continue
                else:
                    clean()
                    break
         elif isbn not in books:
            print("Sorry, the book is not in the list of books.")
    elif user=="3":
       while True:
          in_isbn=input("Enter ISBN to check in: ")
          if in_isbn in books:
             if books[in_isbn]["Available"]==False:            
               books[in_isbn]["Available"]=True
               book=books[in_isbn]["Title"]
               print(f"book '{book}' checked in successfully.")
               check_in=input("Do you want to check in another book?(y/n): ").lower()
               if check_in=="y":
                  clean()
                  continue
               else:
                    clean()
                    break
             else:
                 print(f"Sorry,Book '{book}' is not checked out.")
          else:
             print(f"Sorry,Book not found in the catalog.")
             check_in=input("Do you want to check in another book?(y/n): ").lower()
             if check_in=="y":
                  clean()
                  continue
             else:
                    clean()
                    break
    elif user=='4':
       if books:
         print("Library Catalog:")
         for ISBN in books: 
           title=books[ISBN]["Title"]
           author=books[ISBN]["Author"]
           available=books[ISBN]["Available"]
           print(f"ISBN: {ISBN}, Title: {title}, Author: {author},  Available: {available}")
         back=input("Do yo want to go back to the Main menu or exit the program?(y(back)/n(exit))").lower()
         if back=='y':
            clean()
            continue
         else:
            print(" exiting the program?")
            break  

       else: 
         print("The catalog is empty.")
         back=input("Press Enter to go back to the Main menu?:").lower()
         if back=='y':
            clean()
            continue
    elif user=='5':
       print("Exiting the program.")  
       break       
    else: 
      print("Invalid choice. Please try again.")
      input('Press Enter to continue...')
      clean()
      continue