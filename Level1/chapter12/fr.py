import random
import time
import os


 
def Game():
      def draw():
         """"
           ascii draw game
         """
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
      def clean():  
          os.system("cls" if os.name=="nt"else os.system("clear"))
      def gameStart():
          clean()
          print ("Choose a game to start...")
          time.sleep(2)
          print ("1-Froggy\n2-Twenty One\n3-Snake")#choose game
          print(' -------')
          return input().lower()
      def compare():
              
               if total > 21:
                   print("You went over. You lose!")
               elif comp_total > 21 or total > comp_total:
                   print("You win!")
               elif total < comp_total:
                   print("You lose!")
               else:
                   print("Draw!")
      while True:
         cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
         choice = gameStart()
         if choice in ["twenty one", "21", "2"]:#if user choose 21
              print("Starting game...")
              time.sleep(3)
              clean()
              draw()#draw game
              user_cards = [random.choice(cards), random.choice(cards)]#user cards tow cards
              comp_cards = [random.choice(cards), random.choice(cards)]#computer cards tow and one hidden to user
              total = sum(user_cards)#sum of user cards
              comp_total = sum(comp_cards)#sum of computer cards
              print(f"Your cards are [{user_cards}], current score is {total}")
              print(f"Computer's first card is {comp_cards[0]}")#computer first card
              time.sleep(2)
    #if user score less than 21 can get another card if greater to 21 he lose if equal to 21 he win
              while total < 21:
                    askUser=input("Get another card? y/n: ").lower()
                    if askUser=="y":
                       new_card = random.choice(cards) 
                       user_cards.append(new_card)
                       total = sum(user_cards)
                       if total > 21 and 11 in user_cards:#cheak if there is 11 it place it to 1 if total>21
                          user_cards[user_cards.index(11)] = 1
                          total = sum(user_cards)
                       print(f"Your cards are [{user_cards}], current score is {total}")
                       print(f"Computer's first card is {comp_cards[0]}")
                       time.sleep(2)
                    else:
                         break
              print(f"Your final hand: {user_cards} with score {total}")
    #computer get another card if score less than 21
              if comp_total<17:
                   comp_cards.append(random.choice(cards))
                   comp_total = sum(comp_cards)  
                   if comp_total > 21 and 11 in comp_cards:#cheak
                      comp_cards[comp_cards.index(11)] = 1
                      comp_total = sum(comp_cards)   
              print(f"Computer's final hand: [{comp_cards}] with score {comp_total}")
    #compare user score and computer score
              compare()
              time.sleep(6)
Game()       
