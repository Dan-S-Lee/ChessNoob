# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:42:53 2020

@author: danie
"""
import chess_custom as cc
import pandas as pd
import numpy as np
import os
import pathlib

board = cc.Board()
board_array = board.generate_array()