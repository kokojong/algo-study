import sys
s = list(sys.stdin.readline().rstrip())
# rstrip 때문에 틀림..

isTag = False
result = ''
word = ''

for i in s:
    if isTag : # 태그 안에 있는것 (그대로) (< 와 > 는 빼고)
        word += i
        if i == '>': 
            isTag = False
            result += word
            word = ''

    else: # 태그 밖(< 와 > 포함)
        if i == '<':
            isTag = True
            word += i

        elif i == ' ':
            word += i
            result += word # 뒤집은 단어
            word = ''

        else :
            word = i + word

print(result+word) # 남은 word까지 털어주기
