
n = int(input())

dp = []
for _ in range(n):
    # R G B 로 칠한다면
    r, g, b = map(int, input().split())
    dp.append([r, g, b])

# idea : 이전 색으로만 칠하면 안되는거니까 이전색으로 칠한거 + 이번 색으로 칠하는거 를 해서 제일 작은걸 구함
# R로 칠하려고 하면 이전에 G B 로 칠한거 + R로 칠하는것의 최소값
for i in range(1, n):

    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]

    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]

    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[n-1]))  # 그중에서 제일 작은걸 리턴
