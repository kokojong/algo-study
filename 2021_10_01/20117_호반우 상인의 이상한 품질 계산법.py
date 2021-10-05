# 호반우를 적절히 묶어서 제일 비싸게 팔아먹자
# 품질은 중앙값으로 결정된다(짝수일때는 n/2 + 1번째, 홀수일때는 n+1 / 2)
# n = 4 -> 3, n = 5 -> 3, n = 6 -> 4
# 즉, n//2 + 1 번째에 것을 중앙값으로 사용한다.(index는 n//2)

import sys
input = sys.stdin.readline

n = int(input())
cows = list(map(int, input().split()))

# idea 중앙값의 정의에서 2개를 묶는다면(n=2) 무조건 큰값이 중앙값이 된다
# 제일 작은거, 제일 큰거를 묶기, 홀수라면 가운데에서 3개 묶는거랑 진짜 중간값은 따로 세는거랑 비교해서 더 큰값
# 이거 사기아닙니까..

cows.sort()  # 오름차순
result = 0
# 짝수 개라면 더 큰 n/2 개의 소의 품질로 2배가 된다.
if n % 2 == 0:
    for i in range(n//2, n):  # n/2 ~ n-1
        result += 2*cows[i]
# 홀수개라면 가운데 3개를 따로 middle로 정의해보자(그러나 간단한 수를 대입해서 해보면 3개를 한번에 묶는게 더 작거나 같다)
# 결국 가운데꺼는 따로 더해주는것이 더 크다.
else:
    if n == 1:
        result = cows[0]
    else:
        for i in range(n//2+1, n):  # n//2 +1 ~ n-1
            result += 2*cows[i]
        result += cows[n//2]

print(result)
