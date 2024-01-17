"""
ACAYKP
CAPCAK
"""

s1 = input()
s2 = input()

dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

for row in range(1, len(dp)):
    for col in range(1, len(dp[0])):
        if s1[col-1] == s2[row-1]:
            dp[row][col] = dp[row-1][col-1] + 1
        else:
            dp[row][col] = max(dp[row][col-1], dp[row-1][col])

print(dp[-1][-1])