import random


class Board:
    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.columns = columns
        self.mines = mines

        self.board = self._create_board()

        self.mines_spot = set()
        self.dug = set()

    def _create_board(self):
        board = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        return board

    def plant_mines(self):
        mines = self.mines

        # putting mines on boards in while loop until no mines left
        while mines > 0:
            # randomly select field (x, y)
            x = random.randrange(self.rows)
            y = random.randrange(self.columns)

            # check if randomly selected field is a mine already
            # continue will skip rest of the statement in this iteration
            if self.board[x][y] == '*':
                continue

            # assign the mine to selected field
            self.board[x][y] = '*'

            # set of tuples with mines coordinates x,y where x is row, y is column
            self.mines_spot.add((x, y))

            # -1 mine planted
            mines -= 1

        return self.board

    def assign_nearbly_mines_count(self):
        # mine is tuple (x, y)
        for mine in self.mines_spot:
            # row = x colum = y
            row = mine[0]
            col = mine[1]

            # range of colums and rows is +/- 1
            # but not less than 0 - max, nor more - min than self.(r/c) -1
            row_range = range(max(0, row - 1), min(self.rows - 1, row + 1) + 1)
            column_range = range(max(0, col - 1), min(self.columns - 1, col + 1) + 1)
            for r in row_range:
                for c in column_range:
                    # if it's a mine -continue - keep going
                    if self.board[r][c] == '*':
                        continue
                    # if its None set it 1
                    if self.board[r][c] is None:
                        self.board[r][c] = 1

                    # otherwise increase 1
                    else:
                        self.board[r][c] += 1

        return self.board

    def show_board(self):
        print('Board')
        for row in self.board:
            print(row)

    def dig_spot(self, r, c):
        # is valid input - TODO move to validators and implement as validator
        if r not in range(self.rows+1) or c not in range(self.columns+1):
            "Sorry we can't dig there... \n type 'x y' or 'x, y' "

        # add spot to dug set.
        self.dug.add((r, c))

        # if its a boomb - false = gameover
        if self.board[r][c] == '*':
            return False

        # if greater than 0 means near is a bomb - stop digging
        elif self.board[r][c] > 0:
            return True

        # if not a bomb and not greater than 0
        # check neighboring fields
        row_range = range(max(0, r - 1), min(self.rows - 1, r + 1) + 1)
        column_range = range(max(0, c - 1), min(self.columns - 1, c + 1) + 1)
        for r in row_range:
            for c in column_range:
                if (r, c) in self.dug:
                    continue # dont dig where you have done
                self.dig_spot(r, c)

        return True

    def player_board_view(self):
        visible_board = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.columns):
                if (r, c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = ' '
        for row in visible_board:
            print(row)



board = Board(10, 10, 10)
board.plant_mines()
board.assign_nearbly_mines_count()
board.show_board()
print(board.player_board_view())


def play(rows: int, columns: int, mines: int):

    board = Board(rows=rows, columns=columns, mines=mines)
    board.plant_mines()
    board.assign_nearbly_mines_count()

    # while len(board.dug) is less than (board.rows *board.columns)-board.mines:
    while len(board.dug) > (board.rows * board.columns)-board.mines:
        print(board.player_board_view())

    x, y = map(int, input(f'Where would You like to dig? input row, column as ex.: 2,3\n available rows: {rows}, columns {columns}'))
# map input from player || loop until
#     a) validate input to be correct
#     b) check if input is a boom = game over
#     c) check if its a number = display a number
#     d) if its empty dig each next field until find a number
#
# repeat all until:
