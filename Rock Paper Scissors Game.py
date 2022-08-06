import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user = int(input())
print(gameImages[user])

print("Computer chose:")
computer = random.choice([0, 1, 2])
print(gameImages[computer])

def play(user, computer):
    if user == 0:
      return True if computer == 2 else False
    elif user == 1:
      return True if computer == 0 else False
    else:
      return True if computer == 1 else False      

if user == computer:
  print("Its a draw.")
else:
  if play(user, computer):
    print("You win.")
  else:
    print("You lose.")
