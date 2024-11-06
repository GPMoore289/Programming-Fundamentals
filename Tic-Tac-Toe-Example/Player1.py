
# This file contains the code for Player 1 in a Tic-Tac-Toe game. It is intentionally not simplified or generalized to
# attempt to avoid merge conflicts between the partners.
import random

def getValue( board, position ):
    """
    Returns the value at the given position on the board, from the simple 1-9 index.
    """
    return board[ (position - 1) // 3 ][ (position - 1) % 3 ]

def getMove(board):
    """
    Determines the next move for Player 1. Player 1 will always be 'X'.
    
    Since studnets will not have yet learned lists, we will use indicies 1-9 to represent the Tic-Tac-Toe board as follows:

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9

    To avoid requring list notation in this function, we will use the getValue function to get the value at a given position.

    Parameters:
    board (list of list of str): The current state of the Tic-Tac-Toe board.

    Returns:
    integer: The index of the next move between 1 and 9.
    """
    
    # Example of checking for a win in the top row.
    if ( getValue( board, 1 ) == "X" and getValue( board, 2 ) == "X" and getValue( board, 3 ) == " " ):
        return 3

    return random.randint(1, 9) # This is a placeholder. Replace this line with your code.
