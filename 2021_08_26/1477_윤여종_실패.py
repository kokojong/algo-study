import copy
n, m ,l = map(int, input().split())
# n은 이미 있는 휴게소 m은 추가 휴가소, l은 고속도로 길이

buildings = list(map(int, input().split()))
buildings.append(l) # 끝점(여기에는 못 세움(임의로 추가))
buildings.sort()

# 휴게소 간의 간격
distances = [buildings[0]] # 시작~처음 휴게소
for i in range(n):
    distances.append(buildings[i+1] - buildings[i])
# 이때 len 은 n+1이 된다

# idea : 제일 긴 구간의 중간에 휴게소를 추가하기?
# 반례 : 100 의 길이에 2개를 추가한다고 하면 50 -> (25 or 75)를 설치하게 된다(33, 66에 설치하는게 최소)

# idea : 휴게소가 없는 최대의 범위를 먼저 정하고 그걸 올려가면서 최솟값 찾기?
d = l // (n +m) # 가능한 최소의 최대거리
dd = [] # n+m+1 인 경우 중 최대 거리 리스트

while True: 
    copy_buildings = copy.deepcopy(buildings)
    copy_distances = copy.deepcopy(distances)
    
    for i in range(len(copy_distances)):
        if copy_distances[i] > d :
            if i == 0: # 첫 지점이면
                for j in range(copy_distances[i] // d): # 넣을 수 있는 만큼
                    copy_buildings.append( (j+1) * d) # d의 배수만큼 추가
                    
            else : # 첫 지점 이외
                for j in range(copy_distances[i] // d):
                    copy_buildings.append( copy_buildings[i-1] + (j+1) * d)
    copy_buildings.sort()
    
    
       
    new_distances = [copy_buildings[0]] # 시작~처음 휴게소
    for i in range(len(copy_buildings)-1):
        new_distances.append(copy_buildings[i+1] - copy_buildings[i])

    if len(copy_buildings) == n + m + 1 : # 끝점도 포함이라서
        dd.append(max(new_distances))
    
    if len(copy_buildings) < n + m + 1:
        break
    d += 1


print(min(dd))
# 결과가 71, 72로 나옴..

