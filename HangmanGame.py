# A simple Hangman game where players guess letters to reveal a hidden word. Players have limited chances
# to guess before the hangman is fully drawn. The game utilizes a predefined list of words, ASCII art 
# for hangman stages, and basic input/output operations for gameplay.
import random
import hangmanstages
import hangmanwords
logo = ''' 

   _   _                                         
  | | | |                                        
  | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
  |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  | | | | (_| | | | | (_| | | | | | | (_| | | | |
  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                        


'''                                  
print(logo)                                     
words = (hangmanwords.words)
hangman = (hangmanstages.hangman)
generated_word = random.choice(words)
length = len(generated_word)
print("For reference the word is- {}.".format(generated_word))
display = []
for _ in range(length):
    display += "_"
chance = 6
print(hangman[6])

while True:
    guess = input("Guess a letter: ").upper()
    if len(guess) != 1:
        print("Invalid input. Please enter only one letter.")
        continue 
    found = False  
    for i in range(length):
        letter = generated_word[i]
        if letter == guess:
            display[i] = letter
            found = True  
    print(display)
    if "".join(display) == generated_word:#added .join because then we can have value in form abcd rather than "a""b""c""d" and then we can show it is equal
        print("You won!")
        break
    if not found: 
        chance -= 1
        if chance == 5:
            print(hangman[5])
        elif chance == 4:
            print(hangman[4])
        elif chance == 3:
            print(hangman[3])
        elif chance == 2:
            print(hangman[2])
        elif chance == 1:
            print(hangman[1])
            print("last chance or u will die")    
        elif chance == 0:
            print(hangman[0])
    if chance == 0:
        print("You lose! The correct word was: {}".format(generated_word))
        break
    else:
        print("You have {} chances left".format(chance))
    