n, m = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    src, dest = list(map(int, input().split()))
    graph[src].append(dest)
    graph[dest].append(src)

visited = [False] * (n+1)
visited[0] = True

def dfs(cur):
    if visited[cur] == True:
        return
    
    visited[cur] = True
    for next in graph[cur]:
        if visited[next] == False:
            dfs(next)

connected_component = 0
for node in range(1, n+1):
    if visited[node] == False:
        connected_component += 1
        dfs(node)

print(connected_component)