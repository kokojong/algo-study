import sys
inputs = list(sys.stdin.readline())
li = []

# idea : 최솟값이 되려면 최대한 많이 빼야한다.
# - 이후에 나오는 숫자들을 괄호에 묶어서 빼고, 다시 - 가 나온다면 괄호를 연다


num = ""
for i in inputs:
    if i == '-':
        li.append(int(num))
        li.append('-')
        num = ""

    elif i == '+':
        li.append(int(num))
        li.append('+')
        num = ""
    else:  # 숫자
        num += i
li.append(int(num))  # 남은 숫자 까지 털어줌

isMinus = False
num = 0
for i in li:
    if i == '-':
        isMinus = True
    elif i == '+':
        num += 0
    else:
        if isMinus:
            num -= i
        else:
            num += i

print(num)
