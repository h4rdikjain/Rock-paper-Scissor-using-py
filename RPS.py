from random import randint
t = ["Rock", "Paper", "Scissor"]

#initializing computer play
comp = t[randint(0,2)]
player = False

while player == False:
  player = input("Rock, Paper, Scissor?\n" ) 
  if player == comp:
    print("Tie\n")
  elif player == "Rock" :
    if comp == "Paper"  :
        print("you lose",comp ,"covers",player,"\n")
    else:
        print("You WIN!",player ,"Smashes",comp,"\n")
  
  elif player == "Paper" :
    if comp == "Scissor" :
        print("you lose",comp ,"Cuts",player,"\n")
    else:
        print("You WIN!",player ,"covers",comp,"\n")

  elif player == "Scissor":
    if comp == "Rock":
        print("you lose", comp,"smashes", player,"\n")
    else:
        print("you WIN!",player ,"Cuts", comp,"\n")

  else:
      print("THAT'S NOT A VALID PLAY \n")

  player == False
  comp = t[randint(0,2)]
    

