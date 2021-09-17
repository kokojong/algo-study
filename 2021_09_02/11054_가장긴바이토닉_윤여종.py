import sys
n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

# idea : dp 2개로 각각 오름차순, 내림차순을 만들고, 합쳤을때 길이 보기

dp1 = [1 for _ in range(n)]  # 오름차순
dp2 = [1 for _ in range(n)]  # 내림차순
dp = [1 for _ in range(n)]  # 바이토닉

for i in range(1, n):  # 오름차순 dp
    for j in range(0, i):  # i -1 까지
        if nums[i] > nums[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-2, -1, -1):  # 맨뒤에서 2번째 꺼 부터 시작
    for j in range(n-1, i - 1, -1):
        if nums[i] > nums[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(n):
    dp[i] = dp1[i] + dp2[i] - 1  # 본인은 중복

print(max(dp))
