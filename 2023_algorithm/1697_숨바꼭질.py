"""
5 17
"""

from collections import deque

start, target = map(int, input().split())
MAX = 100000
distance = [0] * (MAX+1)
queue = deque([start])

cur = queue.popleft()
while cur != target:
    for new_cur in (cur-1, cur+1, cur*2):
        if (0 <= new_cur <= MAX) and (distance[new_cur] == 0):
            queue.append(new_cur)
            distance[new_cur] = distance[cur] + 1
    cur = queue.popleft()

print(distance[target])