import sys
inputs = list(sys.stdin.readline())

li = []  # str -> list

# idea : 최솟값이 되려면 최대한 많이 빼야한다.
# - 이후에 나오는 숫자들을 괄호에 묶어서 빼고, 다시 - 가 나온다면 괄호를 연다

number = ""
for i in inputs:
    if i == "-":
        li.append(int(number))  # 이전까지 저장하던 숫자를 추가
        li.append("-")
        number = ""  # 초기화

    elif i == "+":
        li.append(int(number))
        li.append("+")
        number = ""

    else:
        number += i
