from tic_tac_toe_class import tic_tac_toe_BASIC

def main():
    """
    Play a game of basic tic-tac-toe by receiving player moves in a loop until the winning conditions are met.
    """
    board = tic_tac_toe_BASIC()
    print("Welcome to the game! There are two players, O and X. \nO goes first. Choose your symbol.")
    while not board.is_game_won():
        board.player_move("O")
        if board.has_player_won("O"):
            print("Player O has won!")
            break
        if board.is_game_drawn():
            print("Game drawn!")
            break
        board.player_move("X")
        if board.has_player_won("X"):
            print("Player X has won!")
            break

if __name__ == "__main__":
    main()

# do a three player version?? 