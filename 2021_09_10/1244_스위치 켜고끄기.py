
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.

# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
# 그 구간에 속한 스위치의 상태를 모두 바꾼다.(자신 포함)

n = int(input())
switches = [2]  # 0번 스위치는 안쓰므로 0 과 1이 아닌값
inputs = list(map(int, input().split()))
for i in range(len(inputs)):
    switches.append(inputs[i])

# print(switches)


def change(x):
    if x == 1:
        return 0
    elif x == 0:
        return 1


tc = int(input())
for _ in range(tc):
    gender, position = map(int, input().split())
    if gender == 1:  # 남자
        for i in range(position, n+1, position):
            switches[i] = change(switches[i])
        # print(switches)

    else:  # 여자
        switches[position] = change(switches[position])
        for i in range(1, min(position - 1, n - position)+1):
            if switches[position + i] == switches[position - i]:
                switches[position+i] = change(switches[position+i])
                switches[position-i] = change(switches[position-i])
            else:
                break

        # print(switches)
for i in range(1, n+1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print()
