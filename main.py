import random
import os

board = [
    ".......",
    ".......",
    ".......",
    ".......",
    ".......",
    "......."
]

def drop_piece(spot, piece):
    #todo - drop a PIECE at the SPOT
    pass

def draw_board():
    for x in range(len(board)):
        print("|" + board[x] + "|")

draw_board()