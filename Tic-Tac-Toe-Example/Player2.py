# Player2.py
#
# author: Stephen Adams
# date  : 2024-10-19
# modified by Graham, 2024-11-7
#
# This file contains the code for Player 2 in a Tic-Tac-Toe game. It is intentionally not simplified or generalized to
# attempt to avoid merge conflicts between the partners
import random

def getValue( board, position ): #returns the character at that position on the board (X, O or nothing)
    """
    Returns the value at the given position on the board, from the simple 1-9 index.
    """
    return board[ (position - 1) // 3 ][ (position - 1) % 3 ]

def winfinder (pos1, pos2, pos3, board):
    if ( getValue( board, pos1 ) == "O" and getValue( board, pos2 ) == "O" and getValue( board, pos3 ) == " " ):
        return pos3
    if ( getValue( board, pos1 ) == "O" and getValue( board, pos2 ) == " " and getValue( board, pos3 ) == "O" ):
        return pos2
    if ( getValue( board, pos1 ) == " " and getValue( board, pos2 ) == "O" and getValue( board, pos3 ) == "O" ):
        return pos1

def losefinder (pos1, pos2, pos3, board):
    if ( getValue( board, pos1 ) == "X" and getValue( board, pos2 ) == "X" and getValue( board, pos3 ) == " " ):
        return pos3
    if ( getValue( board, pos1 ) == "X" and getValue( board, pos2 ) == " " and getValue( board, pos3 ) == "X" ):
        return pos2
    if ( getValue( board, pos1 ) == " " and getValue( board, pos2 ) == "X" and getValue( board, pos3 ) == "X" ):
        return pos1

def ellforkfinder (pos1, pos2, pos3, pos4, board):
    if ( getValue( board, pos1 ) == "O" and getValue( board, pos2 ) == " " and getValue( board, pos3 ) == " " and getValue( board, 5 ) == "O" and getValue( board, pos4 ) == " " ):
        return pos2
    if ( getValue( board, pos1 ) == " " and getValue( board, pos2 ) == " " and getValue( board, pos3 ) == "O" and getValue( board, 5 ) == "O" and getValue( board, pos4 ) == " " ):
        return pos2

def veeforkfinder(board):
    if ( getValue( board, 1 ) == "O" and getValue( board, 3 ) == "O" and getValue( board, 5 ) == " " and getValue( board, 7 ) == " " and getValue( board, 9 ) == " "):
        return 5
    if ( getValue( board, 1 ) == "O" and getValue( board, 7 ) == "O" and getValue( board, 5 ) == " " and getValue( board, 3 ) == " " and getValue( board, 9 ) == " "):
        return 5
    if ( getValue( board, 7 ) == "O" and getValue( board, 9 ) == "O" and getValue( board, 5 ) == " " and getValue( board, 1 ) == " " and getValue( board, 3 ) == " "):
        return 5
    if ( getValue( board, 3 ) == "O" and getValue( board, 9 ) == "O" and getValue( board, 5 ) == " " and getValue( board, 1 ) == " " and getValue( board, 7 ) == " "):
        return 5

def cornerforkfinder(pos1, pos2, pos3, pos4, pos5, board):
    if ( getValue( board, pos1 ) == " " and getValue( board, pos2 ) == "O" and getValue( board, pos3 ) == " " and getValue( board, pos4 ) == "O" and getValue( board, pos5 ) == " " ):
        return pos1
    if ( getValue( board, pos1 ) == " " and getValue( board, pos2 ) == " " and getValue( board, pos3 ) == " " and getValue( board, pos4 ) == " " and getValue( board, pos5 ) == "O" ):
        return pos1

def getMove(board):
    """
    Determines the next move for Player 2. Player 2 will always be 'O'.
    
    Since students will not have yet learned lists, we will use indicies 1-9 to represent the Tic-Tac-Toe board as follows:

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9

    To avoid requiring list notation in this function, we will use the getValue function to get the value at a given position.

    Parameters:
    board (list of list of str): The current state of the Tic-Tac-Toe board.

    Returns:
    integer: The index of the next move between 1 and 9.
    """
    
    a = winfinder(1, 2, 3, board)
    b = winfinder(4, 5, 6, board)
    c = winfinder(7, 8, 9, board)
    d = winfinder(1, 4, 7, board)
    e = winfinder(2, 5, 8, board)
    f = winfinder(3, 6, 9, board)
    g = winfinder(1, 5, 9, board)
    h = winfinder(3, 5, 7, board)

    i = losefinder(1, 2, 3, board)
    j = losefinder(4, 5, 6, board)
    k = losefinder(7, 8, 9, board)
    l = losefinder(1, 4, 7, board)
    m = losefinder(2, 5, 8, board)
    n = losefinder(3, 6, 9, board)
    o = losefinder(1, 5, 9, board)
    p = losefinder(3, 5, 7, board)

    q = ellforkfinder(1, 2, 3, 8, board) #filled<-->empty, target, empty<-->filled, filled, empty
    r = ellforkfinder(1, 4, 7, 6, board)
    s = ellforkfinder(3, 6, 9, 4, board)
    t = ellforkfinder(7, 8, 9, 2, board)

    u = veeforkfinder(board)

    v = cornerforkfinder(1, 2, 3, 4, 7, board) #target, filled, empty, filled, empty
    w = cornerforkfinder(3, 2, 1, 6, 9, board)
    x = cornerforkfinder(7, 4, 1, 8, 9, board)
    y = cornerforkfinder(9, 6, 3, 8, 7, board)

    oo = None
    if getValue( board, 5 ) == " ":
         oo = 5

    moveslist = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, oo]

    for move in moveslist:
        if move != None:
            return move

    return random.randint(1, 9) # This is a placeholder. Replace this line with your code.
"""
    moves = [a, b, c, d, e, f, g, h]

    for move in moves:
        if move != None:
            getMove(move)
            break
"""
