#import packages to extend python just like we extend sublime, or Atom, or VSCode)
from random import randint

# [] this is an array. an array is a special type of container that can hold mulipe items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

# this is the player choice
player = input("Choose rock, paper or scissors: ")


#this will be the Ai choice -> random 
computer = choices[randint(0,2)]

#check to see what the users input
#print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window

print("user chose:" + player)

#validate thate the random choice worked
print("AI chose: " + computer)


if (computer == player):
	print("tie")

	#alaways check for negative conditions first (the losing case)
elif (computer == "rock"):
	if (player == "scissors"):
		print("you lose!")
	else:
		print("you win!")

elif (computer == "paper"):
	if (player == "rock"):
		print("you lose!")
	else:
		print("you win!")

elif (computer == "scissors"):
	if (player == "paper"):
		print("you lose!")
	else:
		print("you win")










