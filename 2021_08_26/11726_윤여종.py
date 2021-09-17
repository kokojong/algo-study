n = int(input())

# 1 -> 1
# 2 -> 2
# 3 -> (1 에다가 가로로 2개) or (2에다가 세로로 1개)
# 4 -> (2 에다가 가로로 2개) or (3에다가 세로로 1개)

dp = [1, 2]

for i in range(2, n):# dp[n-1] 까지 추가해줌(dp의 크기는 n)
    dp.append( (dp[i-2] + dp[i-1]) % 10007 )

print(dp[n-1])