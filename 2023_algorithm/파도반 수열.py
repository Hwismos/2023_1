T = int(input())
dp = [0] * (101)
dp[1:4] = [1,1,1]
dp[4:6] = [2,2]

for _ in range(T):
    N = int(input())
    if N >= 6:
        for i in(range(6, N+1)):
            dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])
