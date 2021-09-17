# 시간초과ㅠ

# import sys
# n = int(sys.stdin.readline())
# startEnd = []  # start, end
# for i in range(n):
#     s, t = map(int, sys.stdin.readline().split())
#     startEnd.append([s, t])

# startEnd.sort(key=lambda x: (x[0], x[1]))  # start, end순으로 빠른순으로 정렬

# cnt = 0
# while startEnd:
#     cnt += 1
#     tmp = []  # 한번에 가능한 강의의 목록
#     endClass = startEnd[0]  # 첫번째 강의의 시작,끝
#     tmp.append(endClass)
#     for i in range(1, len(startEnd)):
#         if startEnd[i][0] >= endClass[1]:  # 다음 강의의 시작시간 >= 이전 강의의 끝나는시간
#             endClass = startEnd[i]  # 마지막 수업을 갱신
#             tmp.append(endClass)

#     for i in tmp:
#         startEnd.remove(i)
# print(cnt)


#######################
# 시간초과가 나는 부분은 검색을 참고함.
# remove등의 작업은 O(n)을 가져서 느림


import sys
import heapq
n = int(sys.stdin.readline())
startEnd = []  # start, end
heap = []

for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    startEnd.append([s, t])

startEnd.sort(key=lambda x: (x[0], x[1]))  # start, end순으로 빠른순으로 정렬

# 해설을 참고함
for i in range(n):
    # 이전 수업의 끝나는 시간이 다음 수업의 시작보다 작거나 같다면
    if len(heap) > 0 and heap[0] <= startEnd[i][0]:
        heapq.heappop(heap)

    heapq.heappush(heap, startEnd[i][1])  # heap에 끝나는 시간을 넣음
    # print(heap)


print(len(heap))
