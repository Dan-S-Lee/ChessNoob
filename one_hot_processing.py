# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:16:04 2020

@author: daniel_lee
"""

import chess
import pandas as pd
import numpy as np

df = pd.read_csv('2010_df.csv')

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


