n , m , r = map(int, input().split())
# n : 행 , m : 열, r : 회전 수

board = [list(map(int, input().split())) for _ in range(n)]

# print(board)

# idea : 각 껍데기..? 별로 돌리자
# 시작점 좌표의 최댓값은 n//2  m //2  중 min -1  (0 ~ min-1)

# idea : 4개의 방향 list에 동시에 업데이트 하기 -> 배열의 크기가 달라서 실패
# idea : r 을 n또는 m으로 나누면 반복을 줄인다 ?? -> n == m 일때만 가능

# idea : 이전값을 저장하고 돌리기
for _ in range(r): # r번 돌림
    for i in range(min(n//2,m//2)): # 껍데기 횟수
        r ,c = i ,i # 행, 열
        tmp = board[r][c]

        for j in range(i+1, n-i): # 왼쪽방향(열 고정,행 바꿈)
            r = j
            before = board[r][c]
            board[r][c] = tmp # 전 위치(0,0에 있던거)
            tmp = before # 이전에 가지고 있던 값을 대입

        # tmp 는 현재 board[n][0] 을 가지고 있음(같은 방식) 
        for j in range(i+1, m-i) : # 아래
            c = j
            before = board[r][c]
            board[r][c] = tmp
            tmp = before

        for j in range(i+1, n-i): # 오른쪽
            r = n-1 - j
            before = board[r][c]
            board[r][c] = tmp
            tmp = before

        for j in range(i+1, m-i):
            c = m-1 - j
            before = board[r][c]
            board[r][c] = tmp
            tmp = before

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()


