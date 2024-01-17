n = int(input())

if n == 1:
    print(0)
elif n < 4:
    print(1)
else:
    answer = [0] * (n+1)
    answer[1] = answer[2] = answer[3] = 1

    for i in range(4, n+1):
        answer[i] = answer[i-1] + 1
        if i % 3 == 0:
            answer[i] = min(answer[i//3] + 1, answer[i])
        if i % 2 == 0:
            answer[i] = min(answer[i//2] + 1, answer[i])

    print(answer[n])
