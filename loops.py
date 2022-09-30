# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end=' ')
#     print()
#
# for i in range(1, 10):
#     print('*'* i)
#
#
# # Valid!
# row = 4
# column = 5
# board = []
# for r in range(row):
#     columns = column
#     board.append([])
#     while columns > 0:
#         board[r].append([])
#         columns -= 1
#
# print(board)

for numbr in range(0, 16):
    print(f'{numbr} / 4 {numbr / 4}')
    # print(f'{numbr} // 4 {numbr // 4}')
    print(f'{numbr} % 4 {numbr % 4}')

# corresponding = [
#     board[x-1][y],
#     board[x+1][y],
#     board[x][y-1],
#     board[x][y+1],
#     board[x-1][y-1],
#     board[x-1][y+1],
#     board[x+1][y-1],
#     board[x+1][y+1]]
# increas the numbers in coresponding fields for 1
corresponding = [
    board[x - 1][y],
    board[x + 1][y],
    board[x][y - 1],
    board[x][y + 1],
    board[x - 1][y - 1],
    board[x - 1][y + 1],
    board[x + 1][y - 1],
    board[x + 1][y + 1]]
for field in corresponding:
    try:
        field
    except IndexError:
        pass
    else:
        if field == '*':
            pass
        else:
            field += 1