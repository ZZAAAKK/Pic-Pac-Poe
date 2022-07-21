#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Pic-Pac-Poe')
root.geometry('450x450+100+50')
root.resizable(False, False)

board = Canvas(root, width=450, height=450)

board.rowconfigure(0, weight=1)
board.rowconfigure(1, weight=1)
board.rowconfigure(2, weight=1)

board.columnconfigure(0, weight=1)
board.columnconfigure(1, weight=1)
board.columnconfigure(2, weight=1)

turnNumber = [0]
cells = []

def new_game():
    for cell in cells:
        cell.configure(
            foreground = 'white' if cell['background'] == 'white' else 'black',
            text = 'e'
        )

    turnNumber[0] = 0

def declare_victory(winner, winningCells):
    for cell in winningCells:
        cell.configure(foreground = 'green')

    if messagebox.askyesno(
        title = 'Game Over',
        message = f"Player '{winner}' is the winner!\n\nPlay again?"
    ):
        new_game()
    else:
        root.quit()

def declare_stalemate():
    if messagebox.askyesno(
        title = 'Game Over',
        message = 'Stalemate!\n\nPlay again?'
    ):
        new_game()
    else:
        root.quit()

def check_victory():
    isStalemate = True

    for i in range(0, 3):
        if cells[i]['text'] != 'e' and cells[i + 3]['text'] != 'e' and cells[i + 6]['text'] != 'e':
            if cells[i]['text'] == cells[i + 3]['text'] == cells[i + 6]['text']:
                isStalemate = False
                declare_victory(cells[i]['text'], [cells[i], cells[i + 3], cells[i + 6]])

    for i in range(0, len(cells), 3):
        if cells[i]['text'] != 'e' and cells [i + 1]['text'] != 'e' and cells[i + 2]['text'] != 'e':
            if cells[i]['text'] == cells[i + 1]['text'] == cells[i + 2]['text']:
                isStalemate = False
                declare_victory(cells[i]['text'], [cells[i], cells[i + 1], cells[i + 2]])

    if cells[0]['text'] != 'e' and cells[4]['text'] != 'e' and cells[8]['text'] != 'e':
        if cells[0]['text'] == cells[4]['text'] == cells[8]['text']:
            isStalemate = False
            declare_victory(cells[0]['text'], [cells[0], cells[4], cells[8]])

    if cells[2]['text'] != 'e' and cells[4]['text'] != 'e' and cells[6]['text'] != 'e':
        if cells[2]['text'] == cells[4]['text'] == cells[6]['text']:
            isStalemate = False
            declare_victory(cells[2]['text'], [cells[2], cells[4], cells[6]])

    if turnNumber[0] == 9 and isStalemate:
        declare_stalemate()

def take_turn(event):
    if event.widget['text'] == 'e':
        event.widget.configure(
            text = 'x' if turnNumber[0] % 2 == 0 else 'o',
            foreground = 'black' if event.widget['background'] == 'white' else 'white'
            )
        turnNumber[0] += 1
        check_victory()

def build_cells():
    for i in range(0, 3):
        for j in range(0, 3):
            cell = Label(
                board,
                background = 'white' if (i + j) % 2 == 0 else 'black',
                foreground = 'white' if (i + j) % 2 == 0 else 'black',
                font = ('Segoe UI', 38),
                text = 'e'
                )
            cell.bind('<1>', take_turn)
            cell.grid(
                row = i,
                column = j,
                sticky = 'nsew'
            )
            yield cell

cells = list(build_cells())

board.pack(
    expand = True,
    fill = BOTH
)

if __name__ == '__main__': mainloop()