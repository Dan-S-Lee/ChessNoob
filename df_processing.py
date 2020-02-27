# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:23:29 2020

@author: daniel_lee
"""

import chess_custom as cc
import pandas as pd
import numpy as np
import os
import pathlib

#get current directory to make compatible for non-windows
current_dir = pathlib.Path('~/documents/python scripts/ChessAI').expanduser().resolve()
os.chdir(str(current_dir))
df_path = pathlib.Path('2010_df.csv')

df = pd.read_csv(df_path)

start_pos = cc.STARTING_FEN
board = cc.Board(fen = start_pos)

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

for square in cc.SQUARES:
    square_piece = board.piece_at(square = square)
    if square_piece:
        piece_sym = square_piece.symbol()
        c = square_piece.color
        board_array[piece_dict[piece_sym], 
                    square//8, 
                    square%8] = 2 * int(c) - 1
board_array = board.generate_array()
print(board_array)

def generate_dic():
    dic = {}
    for i in range(0, 6):
        temp_row_w = [0] * 12
        temp_row_b = [0] * 12
        temp_row_w[i] = 1
        temp_row_b[i + 6] = 1
        dic[piece_list[i]] = temp_row_w
        dic[piece_list[i+6]] = temp_row_b
    return dic

piece_dict = generate_dic()

def one_hot_array(board, dic):
    one_hot = []
    empty_row = [0] * 12
    for square in cc.SQUARES:
        square_piece = board.piece_at(square = square)
        if square_piece:
            piece_sym = square_piece.symbol()
            one_hot.extend(dic[piece_sym])
        else:
            one_hot.extend(empty_row)
    print(len(one_hot))
    return one_hot

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
    move_df['index'] = move_df['index'].astype(str)
    move_df.drop(move_df.tail(1).index, inplace = True)
    return move_df

df['move_clean'] = df['moves'].apply(create_move_df)
game_dict = dict(zip(df.index.values, df['move_clean']))
result_dict = dict(zip(df.index.values, df['result']))

game_dict[0].to_csv('training_ex1.csv')

#def create_training_example(board, moves):
