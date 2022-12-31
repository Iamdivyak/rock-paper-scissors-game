
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

#Write your code below this line 👇
images = [rock, paper, scissors]
print("Welcome to Rock, Papper, Scissors Game")
persion=int(input("What do you choose? Type 0 for Rock, 1 for Papper and 2 for Scissors\n"))
computer = random.randint(0, 2)
print("computer's choice:")
print(images[computer])

if persion>=3:
  print("You typed wrong imput. You lose!")

else:
  print("Your choice:")
  print(images[persion])
  if persion==0 and computer==2:
    print("You win!")
  elif computer==0 and persion==2:
    print("You lose!")
  elif computer>persion:
    print("You lose!")
  elif persion>computer:
    print("You win!")
  elif computer==persion:
    print("It's a Draw")
