
from collections import deque

n, m = map(int, input().split())
# 총 컴퓨터 갯수 n, 관계 수 m
# 신뢰 방향은 단방향 (A가 B를 신뢰하면 B만 해킹해도 된다)
graph = [[] for _ in range(n+1)]  # 0 ~ n 까지 (0은 안씀)

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)  # b만 해킹해도 a가 자동


def bfs(x):
    visited = [0 for _ in range(n+1)]
    visited[x] = 1

    q = deque([x])
    cnt = 1

    while q:
        tmp = q.popleft()

        for i in graph[tmp]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)

    return cnt


cnts = [0]
result = []
for i in range(1, n+1):
    cnts.append(bfs(i))

for i in range(1, n+1):
    if cnts[i] == max(cnts):
        result.append(i)
print(*result)
