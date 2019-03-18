"""
AP Computer Science Principles
Sticks Game
Authors: Nicholas Tran and Dexter To

The goal of the game is to not be the person that takes the last stick.
It is a version of Nim
https://en.wikipedia.org/wiki/Nim
"""
#Initializing the game values with values from somewhere else. Later we specify this to be values from the user, but this could be preset values instead for a more standard game.
def gameInit(maxSticks, maxGet, players):
  print("There are {} sticks in the bundle.".format(maxSticks))
  print("The maximum sticks a player can get is {}".format(maxGet))
  startGame(maxSticks, maxGet, players)
#Starting the game with our initial values and running the game until someone loses.
def startGame(maxSticks, maxGet, players):
  global gameOver
  global sticksLeft
  gameOver = False
  sticksLeft = maxSticks
  while gameOver == False:
    for currentPlayer in range (players):
      sticksLeft = player(currentPlayer, sticksLeft, maxGet)
      print("There are {} sticks left.".format(sticksLeft))
      if sticksLeft <= 0:
        print("Player {}: You lost.".format(currentPlayer + 1))
        gameOver = True
        break
#Interface for player choosing their sticks
def player(playerNum, playerSticksLeft, maxGet):
  while True:
    try:
      getSticks = int(input("Player {}: How many sticks do you want to get? ".format(playerNum + 1)))
      if getSticks > 0 and getSticks <= sticksLeft and getSticks <= maxGet:
        playerSticksLeft -= getSticks
        break
      else:
        if maxGet > sticksLeft:
          print("That value was too small or too large. Enter a number greater than 0 and less than {}.".format(sticksLeft))
        else:
          print("That value was too small or too large. Enter a number greater than 0 and less than {}.".format(maxGet))
    except ValueError:
      print("That was not an integer value. Try again")
  return playerSticksLeft
#Starting the game
repeat = True
#Initializing Game
while repeat:
  while True:
    try:
      userMaxSticks = int(input("How many sticks are in the bundle? "))
      if userMaxSticks > 1:
        break
      else:
        print("That value was too small. Enter a number greater than 1.")
    except ValueError:
      print("That was not an integer value. Try again")
  while True:
    try:
      userMaxGet = int(input("What is the largest amount of sticks one can get? "))
      if userMaxGet > 1 and userMaxGet <= userMaxSticks:
        break
      else:
        print("That value was too small or too large. Enter a number greater than 1 and less than or equal to {}.".format(userMaxSticks))
    except ValueError:
      print("That was not an integer value. Try again")
  while True:
    try:
      players = int(input("How many players are playing? "))
      if players > 1:
        break
      else:
        print("That value was too small. Enter a number greater than 1")
    except ValueError:
      print("That was not an integer value. Try again")
  gameInit(userMaxSticks, userMaxGet, players)
  while True:
    playAgain = input("Play Again? (Y/N): ")
    if playAgain == "Y":
      break
    elif playAgain == "N":
      repeat = False
      break
    else:
      print("You entered a wrong value. Type 'Y' or 'N'")
