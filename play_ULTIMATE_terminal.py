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
