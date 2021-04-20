class tic_tac_toe_BASIC:
    def __init__(self):
        """
        Initialize class variables.
        """
        self.grid = ["free", "free", "free", "free", "free", "free", "free", "free", "free"]
        self.win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]] # if any of these index triples are the same symbol then the game is won 

    def get_grid(self):
        """
        Get the grid variable representing the current state of play.

        Return: list of ints.
        """
        return self.grid

    def update_grid(self, symbol, location_index):
        """
        Update grid variable by inserting the given symbol at the given index.

        param symbol: str - either "free", "O" or "X".
        param location_index: int - index of cell in grid.
        """
        self.grid[location_index] = symbol

    def delete_previous_move(self, location_index):
        pass
    
    def delete_cell(self, location_index):
        """
        Update grid by freeing the cell at the given location.

        param location_index: int - index of cell in grid.
        """
        if location_index in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            self.update_grid("free", location_index)
        else:
            print("invalid location")
        
    def reset_grid(self):
        """
        Free every cell in the grid.
        """
        for i in range(0, 9):
            self.delete_cell(i)

    def player_move(self, symbol):
        """
        Receive a player's move and update the grid accordingly.
        
        param symbol: str - either "O" or "X"
        """
        while True:
            location = int(input(f"Player {symbol} to move. Enter location: "))
            if (location - 1) in [0, 1, 2, 3, 4, 5, 6, 7, 8] and self.grid[location - 1] == "free":
                self.update_grid(symbol, location - 1)
                break
            else:
                print("Invalid location")
    
    def has_player_won(self, symbol):
        """
        Check if any win conditions are met for the given player.

        param symbol: str - either "O" or "X"

        Return: bool.
        """
        for condition in self.win_conditions:
            flag = True
            for index in condition:
                if self.grid[index] != symbol:
                    flag = False
                    break
            if flag:
                return True
        return False

    def is_game_won(self):
        """
        Check if any winning conditions are met by either player.

        Return: bool.
        """
        for symbol in ["X", "O"]:
            if self.has_player_won(symbol):
                    return True
        return False

    def is_game_drawn(self):
        """
        Check if the game is drawn.

        Return: bool.
        """
        return all(text != "free" for text in self.grid) and not self.is_game_won()

class tic_tac_toe_ULTIMATE:
    def __init__(self):
        """
        Initialize class variables.
        """
        self.big_grid = [["free", tic_tac_toe_BASIC()] for i in range(0, 9)] # Contains a basic tic-tac-toe in each cell. The label "free" means that the game within that cell has not been won yet.
        self.win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]] # if any of these index triples have the same symbol label then the game is won.
        self.move_sequence = []

    def get_big_grid(self):
        """
        Get the big_grid variable representing the current overall state of play.

        Return: list of lists.
        """
        return self.big_grid

    def update_big_grid(self, symbol, sub_grid_index, location_index):
        """
        Update big_grid variable by inserting the given symbol at the given index within the given sub-grid.

        param symbol: str - either "O" or "X".

        param sub_grid_index: int - index of big_grid where sub-grid is.

        param location_index: int - location within the sub-grid to put the symbol.
        """
        self.big_grid[sub_grid_index][1].update_grid(symbol, location_index)
        self.move_sequence.append((symbol, sub_grid_index, location_index))

    def is_sub_grid_full(self, sub_grid_index):
        """
        Determine whether a sub-grid has been filled with the symbols "O" and "X".

        param sub_grid_index: int - index of big_grid where sub-grid is.

        Return: bool.
        """
        return all(self.get_big_grid()[sub_grid_index][1].get_grid()[i] != "free" for i in range(0, 9))
    
    def all_sub_grids_full(self):
        """
        Determine whether all sub-grids have been filled with the symbols "O" and "X".

        Return: bool.
        """
        for i in range(0, 9):
            if not self.is_sub_grid_full(i):
                return False
        return True

    def get_non_full_sub_grids(self):
        """
        Find indices of all sub-grids that have at least one free space.

        Return: list of ints.
        """
        non_full_indices = []
        for i in range(0, 9):
            if not self.is_sub_grid_full(i):
                non_full_indices.append(i)
        return non_full_indices

    def has_player_won_sub_grid(self, symbol, sub_grid_index):
        """
        Check if any of the win conditions are met for the given player in the given sub-grid.

        param symbol: str - either "O" or "X".

        param sub_grid_index: int - index of big_grid where sub-grid is.

        Return: bool.
        """
        for condition in self.big_grid[sub_grid_index][1].win_conditions:
            flag = True
            for index in condition:
                if self.big_grid[sub_grid_index][1].grid[index] != symbol:
                    flag = False
                    break
            if flag:
                return True
        return False

    def has_player_won(self, symbol):
        """
        Check if any winning conditions are met for the given player.

        Return: bool.
        """
        for condition in self.win_conditions:
            flag = True
            for index in condition:
                if self.big_grid[index][0] != symbol:
                    flag = False
                    break
            if flag:
                return True
        return False

    def is_game_won(self):
        """
        Check if any winning conditions are met by either player.

        Return: bool.
        """
        for symbol in ["X", "O"]:
            if self.has_player_won(symbol):
                return True
        return False

    def player_move(self, symbol, sub_grid_index):
        """
        Receive a player's move and update the grid accordingly.
        
        param symbol: str - either "O" or "X"
        param sub_grid_index: int - index of big_grid where sub-grid is.
        """
        while True:
            location = int(input(f"Player {symbol} to move. Enter location in sub-grid {sub_grid_index + 1}: "))
            if (location - 1) in [0, 1, 2, 3, 4, 5, 6, 7, 8] and self.big_grid[sub_grid_index][1].grid[location - 1] == "free":
                self.update_big_grid(symbol, sub_grid_index, location - 1)
                break
            else:
                print("Invalid location")

    def is_game_drawn(self):
        """
        Check if the game is drawn.

        Return: bool.
        """
        return self.all_sub_grids_full() and not self.is_game_won()