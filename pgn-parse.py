# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:34:31 2020

@author: danie
"""

import chess
import chess.pgn
import numpy as np
import pandas as pd
import os

data_dir = 'data/'
file_list = [f for f in os.listdir(data_dir)]

game_text = open(data_dir + file_list[0]).read()
game_dict = {}
i = 0

game_list = game_text.split('\n\n')

headers_list = game_list[::2]
move_list = game_list[1::2]

if len(headers_list[len(headers_list)-1]) < 3:
    headers_list = headers_list[:-1] # last item of list is blank for some reason

df_dict = {'headers': headers_list, 'moves': move_list}

game_df = pd.DataFrame(df_dict)

game_df['result'] = game_df['moves'].apply(lambda x: x.split(' ')[-1])
game_df.to_csv(file_list[0].split('_')[1] + '_df.csv')
