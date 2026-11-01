import random
#STANDARD ROCK PAPER SCISSORS GAME

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

# 0 = ROCK
# 1 = PAPER
# 2 =  SCISSORS

user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))

comp = random.randint(0, 2)

game_images = [rock, paper, scissors]

print(game_images[user])
print(f"Computer Chose: {game_images[comp]}")



if(user == comp):
    print("Its a Draw.")

elif(user == 0 and comp == 1):
    print("You Lose.")

elif(user == 0 and comp == 2):
    print("Congrats! You Won.")

elif(user == 1 and comp == 0):
    print("Congrats! You Won.")

elif(user == 2 and comp == 0):
    print("You Lose.")

elif(user == 1 and comp == 2):
    print("You Lose.")

elif(user == 2 and comp == 1):
    print("Congrats! You Won.")

else:
    print("Enter a Valid Choice.")
