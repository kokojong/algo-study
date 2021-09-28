import sys

# 사진틀 갯수 n, 전체 학생의 총 추천 횟수(len(inputs)) m, 추천 받은 학생의 번호
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))
photos = []

for i in inputs:
    if len(photos) < n:
        isIn = False
        for j in range(len(photos)):
            if photos[j][0] == i:
                photos[j][1] += 1  # 추천수 +1
                isIn = True
                break
        if isIn == False:
            photos.append([i, 1])
    # 처음에 이부분 때문에 틀렸는데, 무조건 append를 해주었더니 반례로
    # 1 1 1 이 들어오게 되면 photos = [[1,1],[1,1],[1,1]]이 되어버림
    # 그래서 isIn 이라는 bool을 추가해서 체크하는 과정을 추가했다.

    else:  # 이미 꽉차 있다면
        isIn = False
        for j in range(n):
            if photos[j][0] == i:
                photos[j][1] += 1  # 추천수 +1
                isIn = True
                break

        if isIn == False:
            # 다 돌았는데도 사진틀에 같은게 없다면 (새로운 사람)
            minval = photos[0][1]  # 첫사람 투표수
            for j in range(1, n):
                minval = min(minval, photos[j][1])
                # 최저 득표수
            for j in range(n):
                if photos[j][1] == minval:
                    photos.remove(photos[j])
                    photos.append([i, 1])
                    break

photos.sort(key=lambda x: x[0])
for i in range(len(photos)):
    # n 까지 범위를 하게 된다면 사진틀보다 더 적은 후보가 등록하면 오류 발생
    print(photos[i][0], end=" ")
