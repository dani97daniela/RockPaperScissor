#Rock Paper Scissor Game
from tkinter import * 
#import tkinter as tk
import random


#For this game there will be 2 players, 1 being the computer, and the other being the user.
#The computer player will need the library of random imported.
def computerPick():
    computerRandom = random.choice(["Rock","Paper","Scissor"])
    theComputerResult["text"] = computerRandom
    return computerRandom
            
#This method will return true if player 1 wins with the rules below.
def win():
    player1 = userResult.get()
    print(player1)
    player2 = computerPick()
    computer = player2
   
    match player1:
        case "rock":
            if player2 == "Scissor":
                result = "You Won"
                theResultLabel["text"] = result
            elif player2 == "Rock":
                result = "It's a Tie"
                theResultLabel["text"] = result
            elif player2 == "Paper":
                result = "You Lost"
                theResultLabel["text"] = result
        case "paper":
            if player2 == "Rock":
                result = "You Won"
                theResultLabel["text"] = result
            elif player2 == "Paper":
                result = "It's a Tie"
                theResultLabel["text"] = result
            else:
                result = "You Lost"
                theResultLabel["text"] = result
        case "scissor":
            if player2 == "Paper":
                result = "You Won"
                theResultLabel["text"] = result
            elif player2 == "Scissor":
                result = "It's a Tie"
                theResultLabel["text"] = result
            else:
              result = "You Lost"
              theResultLabel["text"] = result

window = Tk()
title = "Rock Paper Scissors Shoot!"
window.title(title)
window.maxsize(1000,1000) #Max Size the window can expand to
window.config(bg = "sky blue")
              

computerFrame = Frame(window, width = 300, height = 300, bg = "skyblue")
computerFrame.grid(row = 0, column = 0,padx = 10, pady = 5)

middle_Frame = Frame(window,width = 200,height = 300, bg = "sky blue")
middle_Frame.grid(row = 0,column = 1,padx = 10, pady = 5)

userFrame = Frame(window,width = 300, height = 300, bg = "sky blue")
userFrame.grid(row = 0, column = 2,padx = 10, pady = 5)

resultFrame = Frame(middle_Frame,width = 380, height = 200, bg = "sea green")
resultFrame.grid(row = 0, column = 1,padx = 10, pady = 5)

labelForUserPick = "Please Enter your Choice:\n Rock, Paper, or Scissors!!"
theUserPickLabel = Label(userFrame, bg = "sky blue",text = labelForUserPick).grid(row = 0, column = 0, padx = 5, pady = 5)

theResultLabel = Label(resultFrame,bg = "sea green",text = "Result is:\n ")
theResultLabel.grid(row = 1, column = 0, padx =5, pady = 5)
userResult = Entry(userFrame)
userResult.grid(row = 1,column = 0,padx = 5, pady = 5)
labelForComputerPick = "The \nComputer's Pick"
thecomputerPickLabel = Label(computerFrame, bg = "sky blue", text = labelForComputerPick).grid(row = 0, column = 0, padx = 5, pady = 5)

theComputerResult = Label(computerFrame, bg = "sky blue", text = "")
theComputerResult.grid(row = 1, column = 0, padx = 5, pady = 5)
theButton = Button(userFrame, fg = "sky blue", text = "Enter Choice", relief = RAISED, command= win)
theButton.grid(row = 2,column = 0, padx = 2 ,pady = 3)


window.mainloop()
   

    
