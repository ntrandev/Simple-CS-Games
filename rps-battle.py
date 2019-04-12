"""
Rock Payer Scissors Battle by Nicholas Tran
"""
import random
hierarchy = ["rock", "paper", "scissors"]
#Determine winner of rock, paper, scissors
def winner(player, computer):
  return (hierarchy.index(player) - hierarchy.index(computer) + 2)%3
#Determine damage done by winner
def damage(atk, luk):
  crit = random.randint(1, 10)
  if crit < luk:
    print("A Critical Strike!")
    return atk*2
  elif crit > 9:
    print("The Attack Missed!")
    return atk*0.5
  else:
    print("A regular hit")
    return atk
#Generate a random name for the cpu
def nameGen():
  titles = ["Emperor", "Empress", "King", "Queen", "Prince", "Princess", "Duke",
            "Duchess", "Marquis", "Marquess", "Count", "Countess", "Viscount",
            "Viscountess", "Baron", "Baroness", "Knight", "Lady"]
  names = ["Rocks", "Papers", "Scissors"]
  return random.choice(titles) + " " + random.choice(names)
#Allocate stat points on the player
def spec(stat, ptsLeft):
  if ptsLeft > 0:
    while True:
      try:
        statVal = int(input("{}: ".format(stat)))
        if statVal <= ptsLeft and statVal > 0:
          ptsLeft -= statVal
          break
        else:
          print("That is too little or too big.")
      except ValueError:
        print("That was not an integer value. Try again")
  else:
    statVal = 1
  return [statVal, ptsLeft]
#Player class with stats and hp
class player:
  def __init__(self):
    self.name = input("Player Name: ")
    print("Please spec your character, you have 8 skill points and 3 stats (Luck, Vitality, and Attack).")
    self.pts = 8
    self.luk, self.pts = spec("Luck", self.pts)
    self.vit, self.pts = spec("Vitality", self.pts)
    self.atk, self.pts = spec("Attack", self.pts)
    self.hp = self.vit*10
    self.statUpdate()
  def statUpdate(self):
    print("-"*30)
    print("{}".format(self.name))
    print("Rock Paper Scissors Acolyte")
    print("LUK: {}".format(self.luk))
    print("VIT: {}".format(self.vit))
    print("ATK: {}".format(self.atk))
    print("-"*30)
#NPC class for predefined stats and hp
class cpu:
  def __init__(self, name, luk, vit, atk):
    self.name, self.luk, self.vit, self.atk, self.hp = name, luk, vit, atk, vit*10
    self.statUpdate()
  def statUpdate(self):
    print("-"*35)
    print("{}".format(self.name))
    print("Menacing Rock Paper Scissors Expert")
    print("LUK: {}".format(self.luk))
    print("VIT: {}".format(self.vit))
    print("ATK: {}".format(self.atk))
    print("-"*35)
#fight function for characters to battle until one has no hp left
def fight(charOne, charTwo):
  print("Bring the opponent's hp bar down to zero by winning rock, paper, scissors.")
  while charOne.hp > 0 and charTwo.hp > 0:
      print("Select 'rock', 'paper', or 'scissors' by typing one of those words")
      cpuChoice = random.choice(hierarchy)
      userChoice = None
      while userChoice not in hierarchy:
        userChoice = input("Rock, Paper Scissors, Shoot! ")
      print ("{}: {}".format(charTwo.name, cpuChoice))
      victor = winner(userChoice, cpuChoice)
      if victor == 0:
        charTwo.hp -= damage(charOne.atk, charOne.luk)
        print("{}".format(charTwo.name))
        print("HP: {}".format(charTwo.hp))
      elif victor == 1:
        charOne.hp -= damage(charTwo.atk, charTwo.luk)
        print("{}".format(charOne.name))
        print("HP: {}".format(charOne.hp))
      else:
        print("A tie!")
#Initializes a player, level, and starts the game
user = player()
level = 1
repeat = True
while repeat:
  print("You are facing:")
  comp = cpu(nameGen(), random.randint(1, level*2), random.randint(1, level*2), random.randint(1, level*2))
  fight(user, comp)
  if comp.hp <= 0:
    print("You have slain the mighty {}.".format (comp.name))
    again = input("Would you like to fight another opponent? (y/n) ")
    while True:
      if again == "y":
        level +=1
        user.pts = 5 + 3*level
        print("You have {} skill points! Reallocate your points.".format(user.pts))
        user.luk, user.pts = spec("Luck", user.pts)
        user.vit, user.pts = spec("Vitality", user.pts)
        user.atk, user.pts = spec("Attack", user.pts)
        user.hp = user.vit*10
        user.statUpdate()
        break
      elif again == "n":
        repeat = False
        break
      else:
        print("You entered a wrong value. Type 'y' or 'n'")
        again = input("Would you like to fight another opponent? (y/n) ")
  else:
    print("You have been slain by the mighty {}.".format(comp.name))
    again = input("Would you like to start over again? (y/n) ")
    while True:
      if again == "y":
        level = 1
        user.pts = 8
        print("You have {} skill points! Reallocate your points.".format(user.pts))
        user.luk, user.pts = spec("Luck", user.pts)
        user.vit, user.pts = spec("Vitality", user.pts)
        user.atk, user.pts = spec("Attack", user.pts)
        user.hp = user.vit*10
        user.statUpdate()
        break
      elif again == "n":
        repeat = False
        break
      else:
        print("You entered a wrong value. Type 'y' or 'n'")
        again = input("Would you like to start over again? (y/n) ")
