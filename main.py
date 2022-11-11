import random
import os

board = [
    "-------",
    "-------",
    "-------",
    "-------",
    "-------",
    "-------"
]

player_piece = ""
ai_piece = ""
current_turn = ""

game_running = True


def main():
    pick_pieces()

    while game_running:
        draw_board()
        os.system("PAUSE")

        if current_turn == player_piece:
            pass
        if current_turn == ai_piece:
            ai_plays()

def ai_plays():
    pass

def drop_piece(spot, piece):
    #todo - drop a PIECE at the SPOT
    pass

def check_win():
    global board

def pick_pieces():
    global player_piece
    global ai_piece

    choices = ["X", "O"]

    choice_1 = random.choice(choices)
    choices.remove(choice_1)
    choice_2 = choices[0]

    player_piece = choice_1
    ai_piece = choice_2


def draw_board():
    os.system("CLS")
    for x in range(len(board)):
        print("|" + board[x] + "|")
    print(" 1234567 ")

main()
#draw_board()