import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

dp = [nums[0]]

for i in range(1, n):
    dp.append(max(dp[i-1] + nums[i], nums[i]))

print(max(dp))
