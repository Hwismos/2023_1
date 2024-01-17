n = int(input())
times = list(map(int, input().split()))

times.sort()

costed_time = 0
total_time = 0

for time in times:
    costed_time += time
    total_time += costed_time

print(total_time)