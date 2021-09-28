import sys

string = sys.stdin.readline().rstrip()
# rstrip() 을 해주지 않으면 출력 형식에 오류가 뜸(예제를 다 안돌려본 죄...)

answer = ""
word = ""
isTag = False
for s in string:
    if s == '<':
        # < 를 만난거면 이전에 word를 추가하고 초기화
        answer += word
        word = ""
        answer += s
        isTag = True

    elif s == '>':
        answer += s
        isTag = False

    elif s == ' ':
        # 공백을 만난다면 그전에 word를 추가하고 word를 초기화
        if word:
            answer += word
            word = ""
        answer += ' '

    else:
        if isTag:
            answer += s
        else:
            # word에 역순으로 집어넣는 동작
            word = s + word
# word가 남아있는 경우에 털어줌
print(answer+word)
