from collections import deque
n = int(input())

board = []
distance = [[0 * n] * n]

for _ in range(n):
    board.append(list(map(int, input().split())))


print(board)

size = 2
shark = []  # 상어의 위치

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark.append([i, j])
            break

print(shark)


def checkFishes(sharkSize):
    global n
    cnt = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] <= sharkSize:
                cnt += 1

    if cnt == 0:
        return 0
    elif cnt == 1:


def bfs(i, j):
    global board
    global n
    global shark
    global size
    global distance

    # 위, 왼쪽이 우선(for문으로 i j를 돌릴때 먼저 만나는거)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append(shark)

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]

            dis += 1
            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
