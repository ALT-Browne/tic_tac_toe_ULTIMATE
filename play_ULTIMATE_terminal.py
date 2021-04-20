from tic_tac_toe_class import tic_tac_toe_ULTIMATE

def main():
    """
    Play a game of tic-tac-toe ULTIMATE by receiving player moves in a loop until the winning conditions are met.
    """
    board = tic_tac_toe_ULTIMATE()
    print("Welcome to the game! There are two players, O and X.\nO goes first and may start on any sub-grid. After that, the new sub-grid is determined by the location of the previous move! To win a location in the big grid you must win the sub-grid it contains. To win the game you must win the big grid! Choose your symbol.")

    starting_sub_grid = int(input("Player O, choose the starting subgrid: "))
    board.player_move("O", starting_sub_grid - 1)
    while not board.is_game_won():
        board.player_move("X", board.move_sequence[-1][2])
        if board.big_grid[board.move_sequence[-1][1]][0] == "free": 
            if board.has_player_won_sub_grid("X", board.move_sequence[-1][1]):
                board.big_grid[board.move_sequence[-1][1]][0] = "X" # X wins the sub-grid
        if board.has_player_won("X"):
            print("Player X has won!")
            break
        board.player_move("O", board.move_sequence[-1][2])
        if board.big_grid[board.move_sequence[-1][1]][0] == "free": 
            if board.has_player_won_sub_grid("O", board.move_sequence[-1][1]):
                board.big_grid[board.move_sequence[-1][1]][0] = "O" # O wins the sub-grid
        if board.has_player_won("O"):
            print("Player O has won!")
            break

if __name__ == "__main__":
    main()


# Could figure out if it is a draw before all the subgrids are full and end the game straight away, rather than wasting time letting players do pointless moves...

# add option to delete previous move...must be previous one though otherwise the order will be messed up.

# optimise the has player won and is game won functions by ignoring a condition if one of its indices has been checked and failed....

# maybe just make a copy of the winning conditions list and then check each index in the grid once and, along the way, delete the winning conditions containing any index that fails. if there are any conditions remaining at the end then the player has won!
