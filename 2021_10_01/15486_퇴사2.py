# 입력
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# 출력
# 45

import sys
input = sys.stdin.readline

n = int(input())
Time = []
Pay = []
dp = [0] * n

# idea : i일에 일거리가 들어오면 이전에 일을 진행하던 것과 비교를 해야한다?
# dp를 1차원으로 하기에는 좀 부족해서 아마 2차원으로 해야하지 않을까?
# dp[i][j] => i일에서 j일로 갈때의 dp

# idea2 : dp[i] = 이 상담을 진행한다고 했을때의 최댓값?
# 먼저 남은 일정에서 가능한지 보고, 가능하다면 dp[i] ~ dp[i+t] 까지 p를 더한것과 비교해줌
# i(i~i+t) -> dp[i] 에서 max(p, Pay[i]) ? 잘 모르겠다..

# idea3 : 거꾸로 오는 방법? 맨 뒤에꺼부터 오면서 해보기?

for _ in range(n):
    t, p = map(int, input().split())
    Time.append(t)
    Pay.append(p)

# i == n - 1 일때는 따로 처리해주자(처음이라서 dp[i+1] 을 처리하면 index 오류가 날 수 있음
if Time[n-1] == 1:
    dp[n-1] = Pay[n-1]

# 알아낸 공식 : dp[i] = max( dp[i + Time[i]] + Pay[i] , dp[i+1] )

# i + Time[i] 가 n과 똑같은 경우, 작은경우를 나누지 않았다가 index오류와 틀렸습니다를 엄청 받았습니다 ㅎ...
for i in range(n-2, -1, -1):  # 맨끝-1 에서 부터 오기 n-2 ~ 0
    if i + Time[i] == n:  # 남은 일수와 딱 맞다면(이전 dp가 불가능)
        dp[i] = max(Pay[i], dp[i+1])
    elif i + Time[i] < n:  # 이걸 하고 다른 상담도 같이 한다면
        dp[i] = max(dp[i + Time[i]] + Pay[i], dp[i+1])
    else:
        dp[i] = dp[i+1]
# print(dp)
print(max(dp))
