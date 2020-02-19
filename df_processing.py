# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:06:46 2020

@author: danie
"""

import chess
import pandas as pd
import numpy as np

df = pd.read_csv('2019_df.csv')

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
