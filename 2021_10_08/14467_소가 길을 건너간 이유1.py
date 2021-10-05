# 존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고,
# 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.

# 이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자.
# 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.

n = int(input())

cows = [-1 for i in range(11)]  # 0 ~ 10 (처음에 range를 10으로 해서 틀림..ㅎ))
cnt = 0
for i in range(n):
    cow, location = map(int, input().split())

    if cows[cow] == -1:  # 소를 보기 전
        cows[cow] = location
    else:  # 위치가 이미 있다면
        if cows[cow] != location:  # 위치가 서로 다르다면
            cows[cow] = location  # 위치 갱싱
            cnt += 1
print(cnt)
