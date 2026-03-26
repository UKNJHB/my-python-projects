import os
import random
def clean():  
    os.system("cls" if os.name=="nt"else os.system("clear"))
guess_pc=random.randint(1,10)
while True: 
   clean()
    
   if int(input("Guess the number between 1 and 10: "))==guess_pc:
      print("Congratlation your gusee is right ")
      break
   else:
      print('Wrong gess try again.')
      input("Press any key to continue...")
      clean()

