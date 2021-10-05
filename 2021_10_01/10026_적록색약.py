from collections import deque
import sys
import copy
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())
arr = [list(str(input().rstrip())) for _ in range(n)]
arr2 = copy.deepcopy(arr)
for i in range(n):
    for j in range(n):
        if arr2[i][j] == 'R':
            arr2[i][j] = 'G'

visited1 = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]


def bfs(arr, x, y, color, visited):
    global n
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n:
                if arr[xx][yy] == color and visited[xx][yy] == 0:
                    visited[xx][yy] = 1
                    queue.append((xx, yy))
    # cnt += 1
    # 이부분에서 제대로 cnt를 하고 싶은데 방법을 모르겠네요..


cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            bfs(arr, i, j, arr[i][j], visited1)
            cnt1 += 1


cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            bfs(arr2, i, j, arr2[i][j], visited2)
            cnt2 += 1

print(cnt1, cnt2)
# set1 = set([])
# for i in range(n):
#     for j in range(n):
#         set1.add(visited1[i][j])
# cnt1 = len(set1)  # 정상

# set2 = set([])
# for i in range(n):
#     for j in range(n):
#         set2.add(visited2[i][j])
# cnt2 = len(set2)  # 적록 색맹(R 과 G 를 같은 것으로 생각)

# print(visited1)
# print(visited2)
# print(set1, set2)
# print(cnt1, cnt2)
