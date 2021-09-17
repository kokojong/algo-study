import sys
from collections import deque
m, n, h = map(int, input().split())
# 가로, 세로, 높이
# 익은 1 안익은 0 없으면 -1
graph = []
queue = deque([])

for i in range(h):
    board = [] # 가로, 세로 만
    for j in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if board[j][k] == 1:
                # 익은 토마토를 queue에 넣기
                queue.append([i,j,k])
                # h, n ,m 순
    graph.append(board)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
# 순서가 상관 없음

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        xx = x + dx[i]
        yy = y + dy[i]
        zz = z + dz[i]

        if 0 <= xx < h and 0 <= yy < n and 0 <= zz < m and graph[xx][yy][zz] == 0:
            queue.append([xx,yy,zz])
            graph[xx][yy][zz] = graph[x][y][z] + 1
            # 이동 경로 표기(시간)

day = 0 
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0: # 익지 않은것 존재
                print(-1)
                exit(0)
                # 끝까지 돌아도 닿지 않으면
            day = max(day, graph[i][j][k])

print(day-1)