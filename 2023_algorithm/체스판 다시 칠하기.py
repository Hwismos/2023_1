n, m = list(map(int, input().split()))
board = [[] for _ in range(n)]
for i in range(n):
    row = input()
    for column in row:
        board[i].append(column)

right_board_WB = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']]

right_board_BW = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']]

def check_board(start_row, start_col):
    BW_cnt = 0
    WB_cnt = 0
    for i in range(8):
        for j in range(8):
            if board[start_row+i][start_col+j] != right_board_BW[i][j]:
                BW_cnt += 1
            if board[start_row+i][start_col+j] != right_board_WB[i][j]:
                WB_cnt += 1
    return min(BW_cnt, WB_cnt)


redraw_cnt_list = []

for i in range(n-7):
    for j in range(m-7):
        redraw_cnt = check_board(i, j)
        redraw_cnt_list.append(redraw_cnt)
print(min(redraw_cnt_list))
