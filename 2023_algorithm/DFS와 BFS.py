'''
4 5 1
1 2
1 3
3 4
1 4
2 4
'''

nodes, edges, start = list(map(int, input().split()))
graph = [[] for _ in range(nodes+1)]

for _ in range(edges):
    src, dest = list(map(int, input().split()))
    graph[src].append(dest)
    graph[dest].append(src)

graph = list(map(lambda x: sorted(x), graph))

visited_dfs = [False] * (nodes + 1)
visited_dfs[0] = True
answer_dfs = []

def dfs(cur):
    visited_dfs[cur] = True
    answer_dfs.append(cur)

    for next in graph[cur]:
        if visited_dfs[next] == False:
            dfs(next)

visited_bfs = [False] * (nodes + 1)
visited_bfs[0] = True
answer_bfs = []

from collections import deque

def bfs(start):
    q = deque([start])
    visited_bfs[start] = True
    answer_bfs.append(start)

    while len(q) != 0:
        cur = q.popleft()
        for next in graph[cur]:
            if visited_bfs[next] == False:
                visited_bfs[next] = True
                answer_bfs.append(next)
                q.append(next)

dfs(start)
bfs(start)

answer_dfs = ' '.join(list(map(str, answer_dfs)))
answer_bfs = ' '.join(list(map(str, answer_bfs)))

print(answer_dfs)
print(answer_bfs)