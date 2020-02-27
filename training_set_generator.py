# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:21:57 2020

@author: daniel_lee
"""

import chess_custom as cc
import pandas as pd
import time
import math
import h5py
import numpy as np

df = pd.read_csv('training_ex1.csv')
df.set_index(df.columns.values[0], inplace = True)

def positions_tracker(positions_1, positions_2):
    squares_changed = []
    for i in range(len(positions_1)):
        if positions_1[i] != positions_2[i]:
            squares_changed.append(i)
    if len(squares_changed) > 2:
        for i in squares_changed:
            if positions_1[i] % 6 == 0:
                moved_from = i
            if positions_2[i] % 6 == 0:
                moved_to = i
    else:
        if positions_2[squares_changed[0]] == 0:
            moved_from, moved_to = squares_changed[0], squares_changed[1]
        else:
            moved_from, moved_to = squares_changed[1], squares_changed[0]
    return moved_from, moved_to
def generate_training_example(move_set):
    piece_moved = {}
    board = cc.Board(fen = cc.STARTING_FEN)
    positions_train = []
    moved_from_list = []
    moved_to_list = []
    for ind in move_set.index:
        positions_1 = board.positions()
        moveW_str = move_set.loc[ind]['white']
        board.push_san(moveW_str)
        positions_train.append(board.generate_one_hot())
        #piece_moved[2 * ind] = moveW_str[0]
        positions_2 = board.positions()
        
        #append data
        moved_from, moved_to = positions_tracker(positions_1, positions_2)
        moved_from_list.append(moved_from)
        moved_to_list.append(moved_to)
        
        positions_1 = positions_2
        
        moveB_str = move_set.loc[ind]['black']
        board.push_san(moveB_str)
        positions_train.append(board.generate_one_hot())
        positions_2 = board.positions()
        moved_from, moved_to = positions_tracker(positions_1, positions_2)
        moved_from_list.append(moved_from)
        moved_to_list.append(moved_to)
        #piece_moved[2 * ind + 1] = moveB_str[0]

    return np.array(positions_train), np.array(moved_from_list), np.array(moved_to_list)

training_ex1, from_list, to_list = generate_training_example(df)

with h5py.File('training_set.hdf5', 'w') as f:
    x_data = f.create_dataset('game1_x', data = training_ex1)
    y1_data = f.create_dataset('game1_y1', data = from_list)
    y2_data = f.create_dataset('game1_y2', data = to_list)
#training_ex1.totxt()