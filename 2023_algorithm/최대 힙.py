"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""

import heapq

heap = []
result = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            result.append(0)
        else:
            y = heapq.heappop(heap)
            result.append(y)
    else:
        heapq.heappush(heap, -x)

for x in result:
    print(-x)