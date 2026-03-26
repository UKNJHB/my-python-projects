import random
Guess_nmber=int(input("Guess a number between 1 and 10:\n"))
Guess_PC=random.randint(1,10)
while Guess_nmber!=Guess_PC:
    if Guess_nmber>Guess_PC:
        print("Too high!")
        Guess_nmber=int(input("Guess again:\n"))
    else:
        print("Too Low!")
        Guess_nmber=int(input("Guess again:\n"))
       
    
print("Congratulations! You Guessed the number")
        