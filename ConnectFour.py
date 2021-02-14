#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
import random

import sys
import math

PLAYER = 0
AI = 1
COLUMN_COUNT = 7
ROW_COUNT = 6




def create_game_board():
    # Create board and fill positions with zeros
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
    return board


def play_piece(board, row, col, piece):
    #play game
    board[row][col] = piece


def playable_location_control(board, col):
    # if location is 0 this means it is valid
    return board[ROW_COUNT-1][col] == 0


def get_next_row(board, col):
    # find available position for piece
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def game_board(board):
    print(numpy.flip(board, 0))


def winner_check(board, piece):
    #horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True
    # vertical 
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #positive diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # negative diagonal 
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_game_board()
game_over = False
turn = 0

print(game_board(board))
while not game_over:

    # turn on player 1
    if turn == 0:
        col = int(input("Player 1 make your choice (0-6): "))
        if playable_location_control(board, col):
            row = get_next_row(board, col)
            play_piece(board, row, col, 1)
            if winner_check(board,1):
                print("************************************************")
                print("**************Player 1 Wins!!*******************")
                print("************************************************")
                game_over=True

    # turn on player 2
    else:
        col = int(input("Player 2 make your choice (0-6): "))
        if playable_location_control(board, col):
            row = get_next_row(board, col)
            play_piece(board, row, col, 2)
            if winner_check(board,2):
                print("************************************************")
                print("**************Player 2 Wins!!*******************")
                print("************************************************")
                game_over=True

    print(game_board(board))  # show board to players

    turn += 1
    turn = turn % 2  ##for which player is turn

