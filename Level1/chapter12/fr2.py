import random
import os 
import time

def deal_cards():#deal
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):#calculate
    #black jack
    if sum(cards)==21 and len(cards)==2:
        return 0
    #
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
def clean():  
          os.system("cls" if os.name=="nt"else os.system("clear"))
def compare(user_score,computer_score):#compare
    result={
        "draw": "Draw \n\n",
        "user_over":"You went over 21, Sorry\n\n",
        "computer_over":"Computer went over 21, You win\n\n",
        "user_21":"you won with a blackjack\n\n",
        "computer_21":"Sorry, Computer had a blackjack\n\n",
        "user_win":"You win\n\n",
        "user_lose":"You lose\n\n"
    }
    if user_score==computer_score:
        return result["draw"]
    elif user_score>21:
        return result["user_over"]
    elif computer_score>21:
        return result["computer_over"]
    elif user_score==0:
        return result["user_21"]
    elif computer_score==0:
        return result["computer_21"]
    elif user_score>computer_score:
        return result["user_win"]
    else:
        return result["user_lose"]
def game():
    user_cards=[deal_cards() for _ in range(2)]
    computer_cards=[deal_cards() for _ in range(2)]
    game_countinue=True
    while game_countinue:
        user_score=calculate_score(user_cards)
        computer_score =calculate_score(computer_cards)
         
        print(f"\n\nYour cards are {user_cards}, Current score is {sum(user_cards)}")
         
        print(f"Computer's first card s {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21 or computer_score>21:
            game_countinue= False
        else:
            user_needs=input("Get anther card? y/n ").lower()
            if user_needs=="y":
                user_cards.append(deal_cards())
            else:
                game_countinue=False
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)
    time.sleep(1)
    print(f"Your final hand: {user_cards} with score {user_cards}")
    print(f"Computer's final hand: {computer_cards} with score {computer_score}")
     

    print(compare(user_score,computer_score))
    time.sleep(3)
while input("choose a game to star...\n\n1-Froggy\n2-Twenty One\n3-Snake\n-----\n").lower()=="twenty one":
    clean()
    print("""
          



       /\
     .'  `.
    '      `.
 .'          `.
{              }
 ~-...-||-...-~
       ||
      '--`
 _______        _______ _   _ _______   __       ___  _   _ _____ 
|_   _\ \      / / ____| \ | |_   _\ \ / /      / _ \| \ | | ____|
  | |  \ \ /\ / /|  _| |  \| | | |  \ V /      | | | |  \| |  _|  
  | |   \ V  V / | |___| |\  | | |   | |       | |_| | |\  | |___ 
  |_|    \_/\_/  |_____|_| \_| |_|   |_|    ____\___/|_| \_|_____|
                                           |_____|                


""")
    time.sleep(3)
    game()
     