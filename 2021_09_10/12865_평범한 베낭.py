n, k = map(int, input().split())
# 물품수 n, 최대 무게k

# 2차원 dp로 dp[n+1][k+1] 를 만들기
dp = [[0 for _ in range(k+1)] for i in range(n+1)]
for i in range(1, n+1):
    w, v = map(int, input().split())
    # w는 무게, v는 가치
    for j in range(1, k+1):
        if j < w : # 무게 w 아래는 이전 행의 값을 그대로 갖는다.
            dp[i][j] = dp[i-1][j]
        else : 
            # 이전값 , w가 들어오기전 + v 중에 큰값을 채택
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-w] + v)

print(dp[n][k])