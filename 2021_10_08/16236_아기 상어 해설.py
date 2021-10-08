# 참고 : https://yunanp.tistory.com/12
from collections import deque

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:  # 상어라면
            board[i][j] = 0  # 물고기가 없는 것으로 초기화해줌
            sx, sy = i, j  # 상어의 위치
            break

size = 2
move_sum = 0
eat = 0

while True:
    q = deque()
    q.append([sx, sy, 0])
    visited = [[0] * n for _ in range(n)]  # false

    flag = 1e9  # 10 ^ 9
    fishes = []

    while q:
        x, y, count = q.popleft()

        if count > flag:
            break

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]

            if 0 <= xx < n and 0 <= yy < n:
                if board[xx][yy] <= size and visited[xx][yy] == 0:
                    # 먹을수 있는건 더 작은거, 지나갈 수 있는건 작거나 같은거
                    if board[xx][yy] != 0 and board[xx][yy] < size:
                        # 먹을 수 있는 물고기
                        fishes.append([xx, yy, count+1])
                        flag = count
                    visited[xx][yy] = 1
                    q.append([xx, yy, count+1])

    if len(fishes) > 0:  # 먹을 수 있는 물고기가 있다면
        fishes.sort()  # 위쪽, 왼쪽이 우선적이므로
        fish = fishes.pop(0)  # 맨 왼쪽 물고기(우선순위가 높은 물고기)
        x, y, move = fish[0], fish[1], fish[2]
        move_sum += move
        eat += 1
        board[x][y] = 0  # 먹어버림
        if eat == size:  # 내 사이즈만큼 먹으면
            size += 1  # 몸집이 커지고
            eat = 0  # 먹은 수 리셋
        sx, sy = x, y  # 새로운 상어의 위치

    else:  # 먹을게 없으면
        break

print(move_sum)
