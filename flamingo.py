from tkinter import * 
import random

def next_turn(row,column):
    
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

            buttons[row][column]['text'] = player

            status = check_winner()

            if status is True:
                label.config(text="you win!")
            elif status == "Tie":
                label.config(text="Tie!")
            else:
                player = "x" if player=="0" else "0"
                label.config(text="computer's turn")
                window.update()

                computer_move()
    else:
        print("Game not started")
def computer_move():
    global player 
    
    empty = []
    for row in range(3):
        for column in range(3):
           if buttons[row][column]["text"] == "":
               empty.append([row,column])
    
    if empty: 
        row,column = random.choice(empty)
        buttons[row][column]["text"] = player

        status = check_winner()

        if status is True:
            label.config(text="computer wins!")
        elif status == "Tie":
            label.config(text="Tie!")
        else:
            player = "x" if player=="0" else "0"
            label.config(text = "Your Turn")


def player_move():
    global player
    empty = []
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
               empty.append([row,column]) 


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player
        status = check_winner()

        if status is True:
            label.config(text=f"Player {player} wins!")
        elif status == "Tie":
            label.config(text="Tie!")
        else:
            
            player = "X" if player == "0" else "0"
            label.config(text=f"Player {player}'s turn")
           
            if game_mode == "PvC" and check_winner() is False:
                label.config(text="Computer's turn")
                window.update()
                window.after(500, computer_move)  

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
             return True
        

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
             return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            return True
            
    if empty_spaces is False:
        return "Tie"
    
    return False
  
def empty_spaces():
    
    spaces = 9 

    for row in range(3):
        for column in range(3):
            if buttons [row][column]['text'] !="":
                spaces -=1
    if spaces == 0:
        return False 
    else:
        return True
      
def pvp():
    
    global game_mode
    print("Game started")
    game_mode="pvp"

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#f0f0f0")
    if player == players[1]:
        label.config(text="player's turn")
        window.update()

def new_game():
    
    global player
    print("Game started")
    player = random.choice(players)

    label.config(text=player+"turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#f0f0f0")
    
    if player == players[1]:
        label.config(text="player's turn")
        window.update()
        computer_move()
    else:
        label.config(text="player x Turn")
        label.config(text="player 0 Turn")
def pvc(): 
    
    global player 
    #game_mode = "pvc"
    print("game started")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#030058")    
    if players == players[1]:
        label.config(text="player's turn")
        window.update()
        computer_move()
    else:
        label.config(text = "player wins!")
    if players == players[0]:
        label.config(text="computer's turn")
        window.update()
        player_move()
    else:
        label.config(text = "computer wins!")
        
def new_game():
    
    global computer
    print("Game started")
    player = random.choice(players)

    label.config(text="computer"+"turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#f0f0f0")
    
    if player == players[1]:
        label.config(text="computer's turn")
        window.update()
        computer_move()
    else:
        label.config(text="computer's turn")
        label.config(text="player's Turn")
    


def set_pvp():
    global game_mode
    game_mode = "pvp"
    player_move
    if game_mode is True():
        label.config(text="player wins!") 

def set_pvc():
    global game_mode
    game_mode = "pvc"
    label.config(text = computer_move)
    computer_move
    if game_mode is True():
        label.config(text="computer wins!")

window = Tk()
window.title("Tic-Tac-Toe")
pvp_button = Button(text="pvp",font=('consolas',40),command=player_move)
pvc_button = Button(text="pvc",font=('consolas',40),command=computer_move)
pvp_button.pack(side="right")
pvc_button.pack(side="left")
players = ["x","0"]
player = random.choice(players)
buttons = [[0,0,0] , 
            [0,0,0],
           [0,0,0]]
label = Label(text="tic-tac-toe",font = ('consolas',20))
label.pack(side="top")
reset_button = Button(text="restart",font=('consolas',20),command=new_game)
reset_button.pack(side="top")
frame = Frame(window)
frame.pack()
print("Players: ", players[0], players[1])
for row in range(3):
     for column in range(3):
         buttons[row][column] = Button(frame, text="",font=('consolas',40),width=5,height=2,
                                      command = lambda row=row,column=column: next_turn(row,column))
         buttons[row][column].grid(row=row,column=column)
window.mainloop()