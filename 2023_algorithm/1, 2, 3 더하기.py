T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    if N < 4:
        if N == 1:
            answer.append(1)
        if N == 2:
            answer.append(2)
        if N == 3:
            answer.append(4)
    else:
        dp = [0] * (N+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        dp[4] = 7
        for i in range(4, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        answer.append(dp[N])

for x in answer:
    print(x)
