# This is an implementation of the well-known game tic-tac-toe (aka Noughts and Crosses)

## There are two versions here:

- BASIC. The original, which just consists of a 3x3 grid and to win one must make a straight line of 3 with the same symbol ("O" or "X").
  
- ULTIMATE. This more complicated version consists of a main 3x3 grid and 9 3x3 sub-grids, with one associated to each cell of the main grid. To win a main grid cell, a player must win a BASIC version of tic-tac-toe on the associated sub-grid. Furthermore, most of the time, a player cannot freely choose which cell in the main grid to play in. They must play in the cell corresponding to the position of the sub-grid cell previously played. I have also chosen the allow players to continue playing in sub-grids that have already been won, which will still determine which sub-grid the next player must play in. There is another version which blocks sub-grids as soon as they have been won (even if they aren't full). A player has a free choice of sub-grid if they are sent to a full one.

## There is a terminal script for each version where the game is played completely in the terminal and players use the numbers 1-9 to make thier moves. I have also used pygame to create a gui script for each version.