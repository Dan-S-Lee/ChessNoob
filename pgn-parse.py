# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:34:31 2020

@author: danie
"""

import chess
import chess.pgn
import numpy as np
import pandas as pd

game_text = open('data/ficsgamesdb_2019_standard2000_nomovetimes_115366.pgn')
game_dict = {}
i = 0
game_df = pd.DataFrame(columns = ['Game', 'Moves', 'Result'])
while True:
    game = chess.pgn.read_game(game_text)
    if game is None: break
    game_line = []
    game_line.append('Game{}'.format(i))
    game_line.append(game.board().variation_san(game.mainline_moves()))
    game_line.append(game.headers['Result'])
    game_df.loc[len(game_df)] = game_line
    i+=1
game_df.to_csv('2019_df.csv')
