
n , m = map(int, input().split())
# n은 행, m은 열

Board = [ [0 for _ in range(m+2)] for i in range(n+2) ]
# 가로, 세로에 2줄씩 추가해서 탐색시에 오류 없도록 
visited = [ [0 for _ in range(m+2)] for i in range(n+2) ]
# 방문 여부 
distance = [ [0 for _ in range(m+2)] for i in range(n+2) ]
# 이동한 거리 저장
for i in range(1,n+1): # 입력 받기(처음과 끝은 빼놓고)
   input_list = list(map(int, input()))
   for j in range(1,m+1):
       Board[i][j] = input_list[j-1]

dx, dy = [0,0,1,-1], [1,-1,0,0] # 우 좌 하 상
queue = [[1,1]] 
visited[1][1] = 1
distance[1][1] = 1 # 처음에 시작하면 거리가 1
# 스타트를 1,1로 시작(행, 열에 추가를 해서)

while queue :
    x, y = queue.pop(0) # queue라서 맨앞에꺼
        
    if x == n and y == m :
        # 원하는 위치에 도달
        print(distance[n][m])
        break

    for i in range(4):
        xx, yy= x+dx[i] , y+dy[i]
        if visited[xx][yy] == False and Board[xx][yy] == 1:
            # 아직 방문 안하고 갈수있으면
            queue.append([xx,yy])
            distance[xx][yy] = distance[x][y] + 1 
            visited[xx][yy] = 1

# for dis in distance:
#     print(dis)