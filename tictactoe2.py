from tkinter import * 
import random

def set_pvp():
    global game_mode
    game_mode = "pvp" 

def player_move():
    global player
    empty = []
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                empty.append([row,column]) 

def set_pvc():
    global game_mode
    game_mode = "pvc"

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

def next_turn(row, column):
    global player, game_mode
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player
        status = check_winner()

        if status is True:
            label.config(text=f"Player {player} wins!")
        elif status is False:
            if game_mode == "pvp":
                player = "X" if player == "0" else "0"
                label.config(text=f"Player {player}'s turn")
            else:
                player = "x" if player=="0" else "0"
                label.config(text="computer's turn")
                computer_move()
        else:
            label.config(text = "Tie")
        window.update()
                
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
            
    if empty_spaces() is False:
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
        player_move()
    else:
        label.config(text="player x Turn")
        label.config(text="player o  Turn")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","0"]
player = random.choice(players)
buttons = [[0,0,0] , 
          [0,0,0],
           [0,0,0]]

game_mode = None
def set_mode(mode):
    """Sets the game mode and transitions to the game board."""
    global game_mode
    game_mode = mode

    menu_frame.destroy()

    initialize_game_board()
def initialize_game_board():
    """Generates the game grid and header labels dynamically."""
    global label
    
    # Build your header labels
    label = Label(window, text="tic tac toe", font=('consolas', 40))
    label.pack(side="top")

    reset_button = Button(window, text="restart", font=('consolas', 40), command=new_game)
    reset_button.pack(side="top")

    
    frame = Frame(window)
    frame.pack()

    print("Players: ", players[0], players[1])
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(
                frame, text="", font=('consolas', 40), width=5, height=2,
                command=lambda row=row, column=column: next_turn(row, column)
            )
            buttons[row][column].grid(row=row, column=column)
menu_frame = Frame(window)
menu_frame.pack(pady=50)

menu_label = Label(menu_frame, text="Select Game Mode", font=('consolas', 35))
menu_label.pack(pady=20)


pvp_button = Button(
    menu_frame, text="Player vs Player (PvP)", font=('consolas', 20), 
    width=25, height=2, command=lambda: set_mode("pvp")
)
pvp_button.pack(pady=10)

pvc_button = Button(
    menu_frame, text="Player vs AI (PvC)", font=('consolas', 20), 
    width=25, height=2, command=lambda: set_mode("pvc")
)
pvc_button.pack(pady=10)
def show_switch_button():
    """Generates the Switch Mode button when the game completes."""
    global switch_button
    if switch_button is None:
        switch_button = Button(
            window,
            text="switch mode",
            font=("consolas", 20),
            command=go_back_to_menu,
        )
        switch_button.pack(side="top", pady=10)
        
def go_back_to_menu():
    global label, reset_button, switch_button, frame, buttons

    label.destroy()
    reset_button.destroy()
    if switch_button:
        switch_button.destroy()
        switch_button = None
    frame.destroy()

    # Clear active grid variables
    buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
frame = Frame(window)
frame.pack()
print("Players: ", players[0], players[1])
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40),width=5,height=2,
                                      command = lambda row=row,column=column: next_turn(row,column))
        window.mainloop()