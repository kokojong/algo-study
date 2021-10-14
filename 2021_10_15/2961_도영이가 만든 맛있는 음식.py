
# 신맛은 곱, 쓴맛은 합
# 신맛과 쓴맛의 차이를 최소화
# 재료는 적어도 하나를 사용

from itertools import combinations
n = int(input())
nums = [i for i in range(0, n)]  # 0 ... n-1  (index)
ingredient = []

for _ in range(n):
    sour, bitter = map(int, input().split())
    ingredient.append([sour, bitter])

# idea : 모든 경우를 해본다?

result = sum(ingredient[0])  # 최초의 값


for i in range(1, n+1):  # 1개를 뽑는 경우 ~ n개를 모두 뽑는 경우
    posibles = list(combinations(nums, i))
    # print(posibles)
    for posible in posibles:
        totalSour = 1
        totalBitter = 0

        for j in range(len(posible)):
            # 여기서 실수를 했다. posible[j]를 넣어야 posible 배열에서 가져오는데 그냥 j를 넣어버려서 예상한대로 나오지 않았다.
            totalSour *= ingredient[posible[j]][0]
            totalBitter += ingredient[posible[j]][1]

        total = abs(totalSour - totalBitter)

        if total <= result:
            result = total
            # print(posible)
            # print(result)

print(result)
