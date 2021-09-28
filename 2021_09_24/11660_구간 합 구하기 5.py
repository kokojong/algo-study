import sys
# 표의 크기 n, 합을 구해야 하는 횟수 m (test case)
n, m = map(int, sys.stdin.readline().split())

board = [[0] for _ in range(n)]  # n 행의 0 으로 된 list
dp = [[0 for i in range(n)] for j in range(n)]  # n*n

for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().split()))

dp[0][0] = board[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + board[i][0]  # 0열
    dp[0][i] = dp[0][i-1] + board[0][i]  # 0행

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i][j]

# print(dp)

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # 0부터가 아닌 1부터임
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    if x1 > 0 and y1 > 0:
        answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    elif x1 == 0 and y1 > 0:
        answer = dp[x2][y2] - dp[x2][y1-1]
    elif x1 > 0 and y1 == 0:
        answer = dp[x2][y2] - dp[x1-1][y2]
    else:  # x1, y1 == 0
        answer = dp[x2][y2]

    print(answer)
