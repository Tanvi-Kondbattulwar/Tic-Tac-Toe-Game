import tkinter as tk

player1_turn = True
player2_turn = False

def button_click(button):
    global player1_turn
    global player2_turn
    if button["text"] == " " and player1_turn == True:
        button["text"] = "X"
        player1_turn = False
        player2_turn = True
    elif button["text"] == " " and player2_turn == True:
        button["text"] = "O"
        player1_turn = True
        player2_turn = False
    check_for_winner()

def check_for_winner():
    # Check rows
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        # Check columns
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        # Check diagonals
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        winner_label.config(text="Player 1 wins!")
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          # Check columns
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
          # Check diagonals
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
          winner_label.config(text="Player 2 wins!")
    else:
        winner_label.config(text="Its a Draw :(")
          
root = tk.Tk()
root.title("Tic Tac Toe")

button1 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button1))
button2 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button2))
button3 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button3))
button4 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button4))
button5 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button5))
button6 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button6))
button7 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button7))
button8 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button8))
button9 = tk.Button(root, text=" ", padx=40, pady=20, command=lambda: button_click(button9))

# Put buttons on the screen
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

winner_label = tk.Label(root, text=" ")
winner_label.grid(row=4, column=0, columnspan=3)

root.mainloop()