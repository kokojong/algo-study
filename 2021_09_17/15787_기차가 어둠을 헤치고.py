from collections import deque
n, m = map(int, input().split())
# 기차수, 명령수
trains = [[0 for _ in range(21)] for i in range(n+1)]
posible = []

for _ in range(m):
    command = list(map(int, input().split()))
    # 1 i x꼴
    if command[0] == 1:
        trains[command[1]][command[2]] = 1

    elif command[0] == 2:
        trains[command[1]][command[2]] = 0

    elif command[0] == 3:
        tmp = deque(trains[command[1]])
        tmp.appendleft(0)
        tmp.pop()
        trains[command[1]] = list(tmp)

        # 한칸씩 뒤로 가고 맨 뒤는 삭제

    elif command[0] == 4:
        tmp = deque(trains[command[1]])
        tmp.append(0)
        tmp.popleft()
        tmp[0] = 0  # 이부분을 안써서 틀리다고 나왔음...
        trains[command[1]] = list(tmp)
        # 한칸씩 당기고 맨앞은 삭제, 0번째는 0으로 고정

count = 0
for i in range(1, n+1):
    if trains[i] not in posible:
        posible.append(trains[i])
        count += 1

print(count)
