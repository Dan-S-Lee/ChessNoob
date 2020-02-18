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

white_dict = {}
black_dict = {}

for i in range(0, len(white_list)):
    white_row = [0] * 6
    black_row = [0] * 6
    white_row[i] = 1
    black_row[i] = -1
    white_dict[white_list[i]] = white_row
    black_dict[black_list[i]] = black_row
