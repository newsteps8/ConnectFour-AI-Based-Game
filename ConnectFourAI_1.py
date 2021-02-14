#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import random

ROW_COUNT = 6
COLUMN_COUNT = 7
AI = 2
PLAYER = 1


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


def evaluation_1(board, piece):
  
    three_score = consecutive_three(board, PLAYER) * 10000
   
    two_score = consecutive_two(board, PLAYER) * 100
  
    AI_three_score = consecutive_three(board, AI) * 10000
  
    AI_two_score = consecutive_two(board, AI) * 100

    # Calculate final score of AI and PLAYER
    score = AI_two_score + AI_three_score - two_score - three_score

    return score


def consecutive_two(board, piece):
    #  # the number of two in a row piece has
    count_two_pieces = 0
    for r in range(ROW_COUNT-1):
        for c in range(COLUMN_COUNT-1):
            if c < COLUMN_COUNT-3:
                #horizantal right
                if board[r][c] == board[r][c+1] == piece and board[r][c+2] == board[r][c+3] == 0:
                    count_two_pieces += 1
                if r < ROW_COUNT-3:
                    #diagonal right
                    if board[r][c] == board[r+1][c+1] == piece and board[r+2][c+2] == board[r+3][c+3] == 0:
                        count_two_pieces += 1
            if c >= 3:
                #horizantal left
                if board[r][c] == board[r][c-1] == piece and board[r][c-2] == board[r][c-3] == 0:
                    count_two_pieces += 1
                if r < ROW_COUNT-3:
                    #diagonal left
                    if board[r][c] == board[r+1][c-1] == piece and board[r+2][c-2] == board[r+3][c-3] == 0:
                        count_two_pieces += 1
            if r < ROW_COUNT-3:
                #vertical
                if board[r][c] == board[r+1][c] == piece and board[r+2][c] == board[r+3][c] == 0:
                    count_two_pieces += 1
    return count_two_pieces

def consecutive_three(board, piece):
     # the number of three in a row piece has
    count_three_pieces = 0
    for r in range(ROW_COUNT-1):
        for c in range(COLUMN_COUNT-1):
            if c < COLUMN_COUNT-3:
                #horizantal right
                if board[r][c] == board[r][c+1] == board[r][c+2] == piece and board[r][c+3] == 0:
                    count_three_pieces += 1
                if r < ROW_COUNT-3:
                    #diagonal right
                    if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == piece and board[r+3][c+3] == 0:
                        count_three_pieces += 1
            if c >= 3:
                #horizantal left
                if board[r][c] == board[r][c-1] == board[r][c-2] == piece and board[r][c-3] == 0:
                    count_three_pieces += 1
                if r < ROW_COUNT-3:
                    #diagonal left
                    if board[r][c] == board[r+1][c-1] == board[r+2][c-2] == piece and board[r+3][c-3] == 0:
                        count_three_pieces += 1
            if r < ROW_COUNT-3:
                #vertical
                if board[r][c] == board[r+1][c] == board[r+2][c] == piece and board[r+3][c] == 0:
                    count_three_pieces += 1
    return count_three_pieces


def minimax(board, depth,maximizingPlayer):
    # playable locations
    playable_locations = find_playable_locations(board)
    # Check if game is over or not
    is_terminal, winner = check_game_over(board)
    if depth == 0 or is_terminal:
        # if game over
        if is_terminal:
            # If AI win return 1000000 score
            if winner == AI:
                return (None, 1000000)
            # If Player win return -1000000 score
            elif winner == PLAYER:
                return (None, -1000000)
            else:
                # If no one win ,return 0 score
                return (None, 0)
        else:
            # If depth equals 0 return evaluation score
            return (None, evaluation_1(board, AI))
    if maximizingPlayer:
        value = float("-inf")
        column = random.choice(playable_locations)
        for col in playable_locations:
            row = open_row(board, col)
            # Create a temp board
            temp_board = board.copy()
            # simulation
            play_piece(temp_board, row, col, AI)
            # until terminal or deepest board state
            new_score = minimax(temp_board, depth-1, False)[1]
            if new_score > value:
                value = new_score
                column = col
           
        return column, value

    else:
        value = float("inf")
        column = random.choice(playable_locations)
        for col in playable_locations:
            row = open_row(board, col)
            # Create a temp board
            temp_board = board.copy()
            # simulation
            play_piece(temp_board, row, col, PLAYER)
            #until terminal or deepest board state
            new_score = minimax(temp_board, depth-1, True)[1]
            if new_score < value:
                value = new_score
                column = col
            
        return column, value
    
def open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def find_playable_locations(board):
    # all playable locations
    playable_locations = []
    for col in range(COLUMN_COUNT):
        # If location is available
        if playable_location_control(board, col):
            # position is added to playable locations
            playable_locations.append(col)
    return playable_locations


def game_board(board):
    print(numpy.flip(board, 0))


def check_game_over(board):
    # Check if game is over 
    
    if winner_check(board, PLAYER):
        return True, PLAYER
    
    if winner_check(board, AI):
        return True, AI
    
    if len(find_playable_locations(board)) <= 0:
        return True, 0
    return False, -1


def winner_check(board, piece):
    # Check for win
    # horizontal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # diagonal right
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # diagonal left
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


game_over = False
board = create_game_board()

turn = 0
print(board)

# Game Loop
while not game_over:
    if turn == 0:
        # Take input from player
        col = int(input("Player move (1,7) :"))
        # if input is valid
        if playable_location_control(board, col-1):
            print("PLAYER MOVE")
            row = get_next_row(board, col-1)
            # Make move
            play_piece(board, row, col-1, PLAYER)
            # Pass turn to AI
            turn = 1
            game_board(board)
            if winner_check(board, PLAYER):
                print("PLAYER WINS!")
                game_over = True

            print("----------")
        else:
            print("Column is full")
    else:
        print("AI MOVE")
       
        col, minimax_score = minimax(board, 3, True)
        if playable_location_control(board, col):
            row = get_next_row(board, col)
            play_piece(board, row, col, AI)
            turn = 0
            game_board(board)
            if winner_check(board, AI):
                print("AI WINS!")
                game_over = True
            print("----------")
        else:
            print("Column is full")

