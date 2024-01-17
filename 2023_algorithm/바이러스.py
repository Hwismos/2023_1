N = int(input())
P = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited[0] = True

for _ in range(P):
    _from, _to = list(map(int, input().split()))
    graph[_from].append(_to)
    graph[_to].append(_from)

def dfs(_from):
    visited[_from] = True
    if len(graph[_from]) == 0:
        return
    for _to in graph[_from]:
        if visited[_to] == False:
            dfs(_to)

dfs(1)
print(visited[2:].count(True))