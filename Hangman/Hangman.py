import random
import _hangman
import _hangmanWords
import platform   
import os 

def clear():  
    # Check if the platform is Windows or linux
# If Platform is Windows then run command os.system(‘cls’) else os.system(‘clear’)
    if(platform.system().lower()=="windows"):
        cmdtorun='cls'
    else:
        cmdtorun='clear'   
    
    os.system(cmdtorun)

print(_hangman.logo)

chosenWord = random.choice(_hangmanWords.wordList)
display = ['_' for letter in chosenWord]
blanks = len(display)
lives = 6

def findAndUpdate(guess, chosenWord, display, blanks):
  found = False
  for index, letter in enumerate(chosenWord):
    if guess == letter:
      display[index] = letter
      blanks -= 1
      found = True
  return blanks, found
    

endOfGame = False
guessed = {}
while not endOfGame and lives > 0:
  guess = input("Guess a letter: ").lower()
  clear()
  
  if guess not in guessed:
    guessed[guess] = True
    blanks, found = findAndUpdate(guess, chosenWord, display, blanks)
    
    endOfGame = blanks == 0
    if not found:
      lives -= 1
      print(f'\n{guess} is not in the word. You lose a life.')
      
    print('\n', ' '.join(display))
  else:
    print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
    lives -= 1

  print(_hangman.stages[lives])

if endOfGame:
  print("Congratulations! You Win")
else:
  print('Hanged! Better luck next time')
