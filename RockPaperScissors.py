import random


#For this game there will be 2 players, 1 being the computer, and the other being the user.
#The computer player will need the library of random imported.

def play():
    #the player will input any of the options from the instructions above
    player = input("Please choose one:'r' for rock,'s' for scissor,'p' for paper: ")
    computer = random.choice(['r','p','s'])
    
    if player == computer:
        return 'Its a tie'
    
    if win(player,computer):
        return "You won!"
    
    return "You lost!"
            
#This method will return true if player 1 wins with the rules below.
def win(player1,player2):
    if(player1 == 'r' and player2 =='s'):
        return "Rock beats scissors"
    if(player1 =='p' and player2 =='r'):
        return "Paper beats rock"
    if(player1 =='s' and player2 == 'p'):
        return "Scissor beats paper"
    

 
print(play())       

    
