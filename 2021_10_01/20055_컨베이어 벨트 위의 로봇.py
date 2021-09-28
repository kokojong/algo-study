from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 내구도가 0 인게 k개 이상이면 종료
array = list(map(int, input().split()))
A = deque(array)
robot = deque([0]*(n))  # 어차피 내리는 위치까지 밖에 못감.(심지어 내리는 위치에 도달하면 바로 내림)


cnt = 0

while True:
    cnt += 1

    # 1단계 로봇과 벨트를 1칸씩 이동
    # 마지막 칸에서는 로봇이 내려간다
    A.rotate(1)
    robot.appendleft(0)
    robot.pop()  # 갯수를 맞춰줌
    robot[-1] = 0  # 마지막 칸에 도착하면 바로 내림

    # 2단계 올라간 로봇의 이동
    for i in range(n-2, -1, -1):  # 거꾸로 오는거 # n-2 ~ 0 (n-1에는 로봇이 이미 내려갔음)
        if robot[i] == 1:  # 로봇이 있다면
            if robot[i+1] == 0 and A[i+1] >= 1:  # 다음칸에 로봇이 없고, 다음칸의 내구도가 남아있다면
                # 다음 칸으로 이동 (단, n-2 에서 n-1로 가면 내구도 깎고 바로 내림)
                if i == n-2:
                    robot[i] = 0
                    robot[i+1] = 0
                    A[i+1] -= 1
                else:
                    robot[i] = 0
                    robot[i+1] = 1  # 로봇을 이동
                    A[i+1] -= 1

    # 3단계 올리는 위치의 내구도가 0이 아니라면 로봇을 올림
    if A[0] >= 1:
        robot[0] = 1
        A[0] -= 1

    # 4단계 내구도가 0인 칸의 개수가 k 이상이라면 종료, 아니라면 다시 진행
    zero = A.count(0)
    if zero >= k:
        break
print(cnt)
