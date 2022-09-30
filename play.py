import random


# rows = 4
# columns = 5
#
# board = [[[] for c in range(columns)] for r in range(rows)]


class Board:
    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.columns = columns
        self.mines = mines

        self.board = self._create_board()

        self.mines_spot = set()


    def _create_board(self):
        board = [[None for column in range(self.columns)] for row in range(self.rows)]
        return board

    def plant_mines(self):
        # create board under variable board
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
            self.mines_spot.add((x, y))
            mines -= 1

        return self.board

    def assign_nearbly_mines_count(self):
        for mine in self.mines_spot:
            row = mine[0]
            col = mine[1]
            board.show_board()
            for r in range(max(0, row-1), min(self.rows-1, row+1)+1):
                for c in range(max(0, col-1), min(self.columns-1, col+1)+1):
                    if self.board[r][c] == '*':
                        continue
                    if self.board[r][c] is None:
                        self.board[r][c] = 1
                    else:
                        self.board[r][c] += 1

        return self.board
        # # for each row and column,
        # for rc in self.mines_spot:
        #     if self.board[rc[0]][rc[1]] == '*':
        #         continue

            # self.board[rc[0]][rc[1]] = self.count_neighboring_mines([rc[0]], [rc[1]])


    # def count_neighboring_mines(self, row, col):
    #     number_of_mines = 0
    #     for r in range((row-1), (row+2)):
    #         for c in range((col - 1), (col + 2)):
    #             if self.board[r][c] == '*':


    def show_board(self):
        print('Board')
        for row in self.board:
            print(row)


board = Board(10, 10, 10)
board.plant_mines()
board.assign_nearbly_mines_count()
board.show_board()




# randomly place mine, each field around mine (if exist) increase of number 1

# map input from player || loop until
#     a) validate input to be correct
#     b) check if input is a boom = game over
#     c) check if its a number = display a number
#     d) if its empty dig each next field until find a number
#
# repeat all until:
