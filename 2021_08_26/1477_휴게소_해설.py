n, m ,l = map(int, input().split())
buildings = list(map(int, input().split()))
buildings.append(0)
buildings.append(l-1) # 끝점인데 여기는 못세움

buildings.sort()

start = 0
end = l -1 # 끝점에 못세움

while start <= end:
    mid = (start + end) //2 # 소수가 가능해서 버림
    cnt = 0 # 새로 설치한 수

    for i in range(len(buildings) - 1) :
        distance = buildings[i+1] - buildings[i]
        if distance > mid: # 거리가 mid 보다 크면
            cnt += (distance - 1) // mid
            # 이부분에서 distance - 1 이유를 모르겠음

    if cnt > m :
        start = mid +1
    else :
        result = mid
        end = mid - 1

print(result)
            

