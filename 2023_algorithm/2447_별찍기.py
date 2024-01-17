"""
27
"""

def recursion(n):
    if n < 1:
        return
    
    for start_row in range(n, N, n*3):
        for start_col in range(n, N, n*3):
            for row in range(start_row, start_row + n):
                for col in range(start_col, start_col + n):
                    stars[row][col] = " "
    
    recursion(n//3)

N = int(input())
stars = [["*" for column in range(N)] for row in range(N)]

recursion(N//3)

for x in stars:
    print("".join(x))
