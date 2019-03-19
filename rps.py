"""
Simple Rock Paper Scissors Game
Attempt to make a more efficient implementation
"""
import random
hierarchy = ["rock", "paper", "scissors"]
def winner(player, computer):
  return (hierarchy.index(player) - hierarchy.index(computer) + 2)%3
#0 is player victory
#1 is computer victory
#2 is a draw
print("Select 'rock', 'paper', or 'scissors' by typing one of those words")
cpuChoice = random.choice(hierarchy)
while True:
  userChoice = input("Rock, Paper Scissors, Shoot! ")
  if userChoice in hierarchy:
    break
victor = {0: "Player Wins", 1: "Computer Wins", 2: "Draw"}
print("The player chose {}".format(userChoice))
print("The computer chose {}".format(cpuChoice))
print(victor[winner(userChoice, cpuChoice)])
