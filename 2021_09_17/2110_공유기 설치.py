n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))

houses.sort()

# 공유기 사이의 거리를
# 이진탐색으로 검색 (몇일지 미리 정하고)
start = 1
end = houses[n-1] - houses[0]
result = 0

while start <= end:
    mid = (start+end) // 2  # gap
    house = houses[0]
    count = 1

    for i in range(1, n):
        if houses[i] >= house + mid:  # mid만큼의 거리 이상 차이가 난다면
            count += 1
            house = houses[i]  # 다음 집으로 기준을 변경

    if count >= c:  # c개 이상의 공유기를 설치함 (조건만족)
        start = mid + 1  # 너무 많은 공유기를 설치한 것 일수도 있어서
        result = mid
    else:  # count < 3 -> 너무 범위를 크게 설정 함(너무 공유기가 적음)
        end = mid - 1

print(result)

# 1 2 4 8 9 에서 해보면
# start = 1, end = 8, mid = 4
# house = 1 (좌표)
# houses[4] = 8 >= 1 +4
# 1 8 (5가 없기 때문에 띄엄 띄엄)
# count = 2
# house = 8

# start = 1, end = 4 - 1 = 3, mid = 2
# 1 4 8 , count = 3

# start = 3, end = 3 , mid =3
# 1 4 8, count = 3
# start = 4, end = 4 가 되어버려서 종료
