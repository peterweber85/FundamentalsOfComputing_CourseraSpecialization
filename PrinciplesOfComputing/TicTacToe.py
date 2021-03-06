"""
Monte Carlo Tic-Tac-Toe Player
"""
import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player


# Add your functions here.
def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player
    by making random moves, alternating between players. The function
    should return when the game is over. The modified board will contain
    the state of the game, so the function does not return anything. In
    other words, the function should modify the board input.
    """
    empty_squares = board.get_empty_squares()
    random_square = random.choice(empty_squares)
    while len(empty_squares) >= 1:
        board.move(random_square[0], random_square[1], player)
        empty_squares.remove(random_square)
        provided.switch_player(player)
        if len(empty_squares) == 0:
            break
        else:    
            random_square = random.choice(empty_squares)

    
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the
    same dimensions as the Tic-Tac-Toe board, a board from a completed
    game, and which player the machine player is. The function should
    score the completed board and update the scores grid. As the function
    updates the scores grid directly, it does not return anything.
    """
    winner = board.check_win()
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if winner == player:            
                if board.square(row,col) == winner:
                    scores[row][col] += SCORE_CURRENT 
                elif board.square(row,col) == provided.switch_player(player):
                    scores[row][col] -= SCORE_OTHER
            elif winner == provided.switch_player(player):
                if board.square(row,col) == winner:
                    scores[row][col] += SCORE_OTHER 
                elif board.square(row,col) == player:
                    scores[row][col] -= SCORE_CURRENT
                                    
    
def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The function
    should find all of the empty squares with the maximum score and randomly
    return one of them as a (row, column) tuple. It is an error to call this
    function with a board that has no empty squares (there is no possible
    next move), so your function may do whatever it wants in that case. The
    case where the board is full will not be tested.
    """
    highest_score = -NTRIALS    
    empty_squares = board.get_empty_squares()
    for row_col in empty_squares:
        score = scores[row_col[0]][row_col[1]]
        if score > highest_score:
            highest_score = score
            index_highest = row_col
    
    return index_highest
    
    
    
def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is,
    and the number of trials to run. The function should use the Monte Carlo
    simulation described above to return a move for the machine player in the
    form of a (row, column) tuple. Be sure to use the other functions you have
    written!
    """
    scores = [[0 for dummy_row in range(board.get_dim())] for dummy_col in range(board.get_dim())]
    for _ in range(trials):
        mc_trial(board, player)
        mc_update_scores(scores, board, player)
    
    get_best_move(board, scores)


#provided.play_game(mc_move, NTRIALS, False)
#poc_ttt_gui.run_gui(dim, provided.PLAYERX, mc_move, NTRIALS, False)

