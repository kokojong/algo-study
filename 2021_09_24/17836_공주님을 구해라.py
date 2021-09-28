n, m, t = map(int, input().split())
# n = row, m = column, t = time
board = []
# 시작점은 (0,0) 공주님은(n,m)
for _ in range(n):
    board.append(list(map(int, input().split())))

# 아이디어 : 칼을 줍는 경우와 줍지 않는 경우로 나눈다!
# 칼을 주우면 바로 공주님에게 돌진, 안주우면 그냥 미로 그자체
# 두 가지 경우를 봤을 때 t시간 내에 가능한 경우가 있는지 확인하기
# 가는데 걸리는 시간이 중요하므로 bfs 문제다!

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 모든 방향을 가는거라서 방향벡터의 순서는 상관이x

visited = [[0] * m for _ in range(n)]
q = []
visited[0][0] = 1
q.append((0, 0))

answer = 10001
# t가 10000 이하이기 때문에 그거보다만 크면 된다.
# answer = 10000으로 했다가 틀림...ㅎ


while q:
    x, y = q.pop(0)
    if board[x][y] == 2:
        # 칼을 주움
        # 공주까지 직선으로 가면 된다.
        answer = (n-1-x) + (m-1-y) + (visited[x][y] - 1)

    if x == n-1 and y == m-1:
        # 공주에게 도달(칼 없이)
        answer = min(answer, visited[x][y] - 1)
        break

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] != 1:
            if visited[xx][yy] == 0:  # 갈 수 있는 곳이면 큐에 넣음
                q.append((xx, yy))
                visited[xx][yy] = visited[x][y] + 1

if answer <= t:
    print(answer)
else:
    print("Fail")
