from collections import deque

n, m, start = map(int,input().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
for tmp in lst:
    tmp.sort()
print(lst)

def dfs(now):
    visited[now] = 1
    print(now, end=' ')
    for num in lst[now]:
        if visited[num] != 1:
            dfs(num)

def bfs(now):
    q = deque()
    q.append(now)
    visited[now] = 1
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for num in lst[cur]:
            if visited[num] != 1:
                visited[num] = 1
                q.append(num)
            
visited = [[0] for _ in range(n+1)]
dfs(start)
visited = [[0] for _ in range(n+1)]
print()
bfs(start)
