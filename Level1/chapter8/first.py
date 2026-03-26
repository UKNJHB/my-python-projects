import random
words=["office","bad","good"]
random_words=random.choice(words)
display=["_"for _ in random_words]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
chance=len(HANGMANPICS)-1
wrong_guesses=0
print("Welcom to our game\nPlease guess a letter:")
print(" ".join(display))
print(HANGMANPICS[0])
wrong_letters=[]
while "_" in display and chance >0 :
    guess=input("Please enter you're guess a letter:").lower()
    if guess in wrong_letters:
            print(f"You already guessed this letter '{guess}'")
            continue
    for position in range(len(random_words)):
        if random_words[position]==guess:
         display[position]=guess
         print(f" Good guess,You have '{chance}' more tries ") 
    if guess not in random_words:
        chance-=1
        wrong_guesses+=1 
        wrong_letters.append(guess)       
        if chance==0:
            print(f"""
            *********
            -You Lose-
            *********
      {HANGMANPICS[wrong_guesses]}  
            The word was '{random_words}'
            """)
            break
        else:
          print(f"Wrong guess '{chance}' chance left\n{HANGMANPICS[wrong_guesses]}")
    print(" ".join(display))
    if  "".join(display)==random_words  :
      print("""
      *********
      -You Win-
      *********
         O   |
        /|\  |
        / \  |
    ==============
      """)