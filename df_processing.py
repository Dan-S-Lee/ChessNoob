# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:06:46 2020

@author: danie
"""

import chess
import pandas as pd
import numpy as np
import os
import pathlib

#get current directory to make compatible for non-windows
current_dir = pathlib.Path('~/.spyder-py3/ChessAI').expanduser().resolve()
os.chdir(str(current_dir))
df_path = pathlib.Path('2019_df.csv')

df = pd.read_csv(df_path)

start_pos = chess.STARTING_FEN
board = chess.Board(fen = start_pos)

row = [0] * 8
board_list = [[row for i in range(0,8)] for j in range(0,6)]
board_array = np.array(board_list)

white_list = ['p', 'n', 'b', 'r', 'q', 'k']
black_list = [l.upper() for l in white_list]

white_list.extend(black_list)
piece_list = white_list

piece_dict = {}

for i in range(0, 6):
    piece_dict[piece_list[i]] = i
    piece_dict[piece_list[i+6]] = i

for square in chess.SQUARES:
    square_piece = board.piece_at(square = square)
    if square_piece:
        piece_sym = square_piece.symbol()
        c = square_piece.color
        print('Square int - {}'.format(square))
        print('Row - {}'.format(square//8))
        print('Column - {}'.format(square%8))
        board_array[piece_dict[piece_sym], 
                    square//8, 
                    square%8] = 2 * int(c) - 1
                    
print(board_array)

piece_dict = {}

empty_row = [0] * 12

for i in range(0, 6):
    temp_row_w = [0] * 12
    temp_row_b = [0] * 12
    temp_row_w[i] = 1
    temp_row_b[i + 6] = 1
    piece_dict[piece_list[i]] = temp_row_w
    piece_dict[piece_list[i+6]] = temp_row_b

one_hot = []
for square in chess.SQUARES:
    square_piece = board.piece_at(square = square)
    if square_piece:
        piece_sym = square_piece.symbol()
        one_hot.extend(piece_dict[piece_sym])
    else:
        one_hot.extend(empty_row)

print(len(one_hot))

def create_move_df(moves: str):
    move_list = moves.replace('.','').split()
    ind_list = move_list[::3]
    white_list = move_list[1::3]
    black_list = move_list[2::3]
    
    #cuts the list off according to the shortest one
    move_len = min(len(ind_list), len(white_list), len(black_list))
    
    ind_list = ind_list[:move_len]
    white_list = white_list[:move_len]
    black_list = black_list[:move_len]
    
    #convert lists into dictionary then dataframe
    move_dict = {'index': ind_list, 'white': white_list, 'black': black_list}
    move_df = pd.DataFrame(move_dict)
    return move_df
