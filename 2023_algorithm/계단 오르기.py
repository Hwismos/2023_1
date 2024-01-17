'''
6
10
20
15
25
10
20
'''

N = int(input())
dp = [0] * (301)
data = [0] * (301)
for i in range(N):
    value = int(input())
    data[i+1] = value

dp[1] = data[1]
dp[2] = data[1] + data[2]

for i in range(3, N+1):
    dp[i] = max(data[i] + data[i-1] + dp[i-3], data[i] + dp[i-2])

print(dp[N])

