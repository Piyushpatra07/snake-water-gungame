import random
def gamewin(you, computer):
  if computer ==you:
    return None
  elif computer == 's':
    if you == 'w':
      return False
    if you == 'g':
      return True
  elif computer == 'w':
    if you == 's':
      return True
    if you == 'g':
      return False
  elif computer == 'g':
    if you == 'w':
      return True
    if you == 's':
      return False 
    
print("Cmputer's turn : snake(s), water(w), gun(g)  ??")    
randomno = random.randint(1, 3)
if randomno == 1:
  computer = 's'
elif randomno == 2:
  computer =  'w'
elif randomno == 3:
  computer = 'g'

you= input("snake(s), water(w), gun(g)")
print("computer choose", computer)
print("you choose", you)
a= gamewin(computer, you)
if a == None:
  print("It is a Tie !!")
elif a:
  print("You Win 😊😊")
else:
  print("You lose 😢")