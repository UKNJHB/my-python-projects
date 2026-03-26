import random
Pc_user=random.randint(1,100)
chanse=5
while chanse>0:
    user=int(input("Etre un nombre entre 1 et 100 VOUS AVES 5 CHANCES:\n"))
    if user==Pc_user:
        print("Bravo")
        print("Pc choisite:"+Pc_user) 
        break
    elif user<Pc_user:
         print("Trop petit")
    else:
         print("Trop grand")
    chanse-=1
    if chanse==0:
            print(f"Perdu vous avez perdu {chanse} Pc choisite {Pc_user}")
            break
    
    print(f" 'faux' choise un atre nombre\n vous avez encore {chanse}")
