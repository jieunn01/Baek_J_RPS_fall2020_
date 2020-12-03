#import packages to extend python just like we extend sublime, or Atom, or VSCode)
from random import randint

# [] this is an array. an array is a special type of container that can hold mulipe items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]


player_lives = 5
ai_lives = 5

total_lives = 5

# define a win or lose function
def winorlose(status):

	print("You", status, "Would you like to try again?")
	choice = input("Y / N : ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time!")
		exit()

	elif choice == "Y" or choice == "y":
		# reset the player lives and the AI livves
		# and set player to False so that our loop will restart
		global player_lives
		global ai_lives
		global player

		player_lives = 5
		ai_lives = 5
		player = False

	else:
		print("Make a valid choice - Y or N")
		# this will generate a bug that we need to fix later
		choice = input("Y / N : ")

# this is the player choice
# player = input("Choose rock, paper or scissors: ")

# Ture or False are Boolean data types -> switch on or off OR 1 or 0 OR Ture or False
player = False

while player == False:
	print("===================*/ RPS GAME */=====================")
	print("computer Lives: ", ai_lives,"/", total_lives)
	print("Player Lives: ", player_lives, "/", total_lives)
	print("======================================================")

	print("Choose your weapon! or type quit to exit\n") #\n : New line

	player = input("Choose rock, paper or scissors: \n")
	# player = True ( it has value rock, paper, scissors) False 

	# if the palyer chose to quit, then exit the game
	if player =="quit":
		print("you chose to quit")
		exit()


	# this will be the Ai choice -> random 
	computer = choices[randint(0,2)]

	# check to see what the users input

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + player)

	# validate thate the random choice worked
	print("AI chose: " + computer)


	if (computer == player):
		print("tie")

	# alaways check for negative conditions first (the losing case)
	elif (computer == "rock"):
		if (player == "scissors"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			ai_lives -= 1

	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose!")
			player_lives -= 1
		else:
			print("you win")
			ai_lives -= 1

	if player_lives == 0:
		winorlose("lost")

	if ai_lives == 0:
		winorlose("won")

		# print("You won! Would you like to try again?")
		# choice = input("Y / N : ")

		# if choice == "N" or choice == "n":
		# 	print("You chose to quit! Better luck next time!")
		# 	exit()

		# elif choice == "Y" or choice == "y":
		# 	# reset the player lives and the AI livves
		# 	# and set player to False so that our loop will restart
		# 	player_lives = 5
		# 	ai_lives = 5
		# 	player = False

		# else:
		# 	print("Make a valid choice - Y or N")
		# 	# this will generate a bug that we need to fix later
		# 	choice = input("Y / N : ")


	print("player lives:", player_lives)
	print("ai lives", ai_lives)

	# make the loop kee runnibng by setting player vack to False
	# unset, so that our loop condition above will evaluate to True

	player = False



