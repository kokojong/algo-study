import sys
input = sys.stdin.readline

meetings = []

n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append([start, end])

meetings.sort(key=lambda x: (x[1], x[0]))
# 끝나는 시간이 우선, 그 다음은 시작시간이 작은것부터 정렬

cnt = 1
endTime = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= endTime:  # 시작가능 하다면
        cnt += 1
        endTime = meetings[i][1]

print(cnt)
