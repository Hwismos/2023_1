"""
2
1
3
2
3
"""

T = int(input())
data = [[] for _ in range(T)]
for t in range(T):
    data[t].append(int(input()))
    data[t].append(int(input()))

for t in range(T):
    K, N = data[t]
    dp = [[0] * (N+1) for _ in range(K+1)]

    for n in range(N+1):
        dp[0][n] = n
    
    for k in range(1, K+1):
        for n in range(1, N+1):
            dp[k][n] = dp[k][n-1] + dp[k-1][n]
    
    print(dp[K][N])