
n = int(input())

# idea BBB -> B, RR -> R로 다 치환
# 시작점과 끝점이 같은가? 로 나눈다. 시작점이 같다면 다 칠하고 중간만 칠하게 한다.

string = list(map(str, input()))
# print(string)
arr = [string[0]]

for i in range(1, len(string)):
    if arr[-1] != string[i]:
        arr.append(string[i])


# 처음과 끝이 같은 경우에는 (len+1) / 2 가 색칠수가 된다.
if len(arr) % 2 == 0:  # 처음과 끝이 다름 B R B R B R -> (BRBRB) R 로 나눈다.
    result = len(arr) // 2 + 1
else:
    result = (len(arr) + 1) // 2

print(result)
