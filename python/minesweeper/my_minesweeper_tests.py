#!/usr/bin/env python
from minesweeper import *


empty_space = MinesweeperSpace(2, 3, ' ', 0)
bomb_space = MinesweeperSpace(1, 1, '*', 0)
print('Empty space: {}'.format(empty_space))
print('Bomb space:  {}'.format(bomb_space))

inp = ["+------+",
       "| *  * |",
       "|  *   |",
       "|    * |",
       "|   * *|",
       "| *  * |",
       "|      |",
       "+------+"]

board = MinesweeperBoard(inp)
print(board)
print(board[0, 0])
