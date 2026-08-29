import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''  _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = input("what will you choose rock, paper, or scissors (R,P,S)")
if user == "R":
      print(rock)
elif user == "P":
      print(paper)
elif user =="S":
      print(scissors)
else :
   print("you didn't choose")

com = random.choice([rock, paper, scissors])
print(com)
if com == rock:
      if user =="R":
            print("it's a draw")
      elif user =="P":
            print("you won")
      else: 
            user=="S"
            print("you lost")

if com == paper:
      if user =="R":
            print("you lost")
      elif user =="P":
            print("it's a draw")
      else: 
            user=="S"
            print("you won")

if com == scissors:
      if user =="R":
            print("you won")
      elif user =="P":
            print("you lost")
      else: 
            user=="S"
            print("it's a draw")
