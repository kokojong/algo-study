import sys
n = int(sys.stdin.readline())

honeys = list(map(int, sys.stdin.readline().split()))

# 처음 생각 -> 벌을 무조건 왼쪽 또는 오른쪽 끝에 붙이기.
# 반례 : 예제3 - 2 5 4 의 최대값은 10이 되어야 하는데 안된다(가운데가 벌통)

# idea2 case를 3개로 나눠서 
# 벌1 벌2 ... 벌통  or 벌1 ... 벌통 ... 벌2 or 벌통 ... 벌1 벌2

# case1 = sum(honeys[2:]) * 2

# 이 부분은 올바름
# if n %2 == 1:
#     # honeys[1] ... 중간 + 중간 ... honeys[-2] (n 이 7이라면 honeys[5까지] 포함해서
#     # 홀수라면 n//2를 2번 더해줌
#     case2 = sum(honeys[1:n//2 + 1]) + sum(honeys[n//2 : n-1]) # n-2까지
# else :
#     # 짝수라면 중간값 2가지 중에 큰 것을 선택
#     # 중간 값이 n //2 일 경우, n//2 - 1 일 경우 중 최댓값
#     case2 = max(sum(honeys[1 : n//2]) + sum(honeys[n//2 -1 : n-2]) , 
#                 sum(honeys[1 : n//2+1] + sum(honeys[n//2 : n-2])) )

# case3 = sum(honeys[:-2])* 2

# print(case1, case2 , case3)

# 여기까지 했는데 예시 1번처럼 하는 경우가 존재함(벌이 붙어있지 않는 경우)가 존재한다

###########################################################################

# 벌1 맨 왼쪽, 벌통 맨 오른쪽 고정, 벌2는 for 문 돌려서?
# 벌1 벌통 벌2 은 무조건 양끝이 최대
# 벌통 맨왼쪽, 벌1 맨 오른쪽, 벌2는 for문? 3가지 

# case 1 벌1 ... 벌2 ... 벌통
case1 = 0
for bee2 in range(1,n-1) : # 벌2는 [1] ~ [n-2]까지 가능
    b1 = sum(honeys[1:]) - honeys[bee2] # 1부터 n-1까지 가다가 벌2만 제거
    b2 = sum(honeys[bee2+1:]) # 벌2는 [bee2 +1] 까지 도착가능
    case1 = max(b1 + b2 , case1) # 더 큰값으로 갱신
    

# case 2 벌1 ... 벌통(중간) .. 벌2
if n %2 == 1:
    # honeys[1] ... 중간 + 중간 ... honeys[-2] (n 이 7이라면 honeys[5까지] 포함해서
    # 홀수라면 n//2를 2번 더해줌
    case2 = sum(honeys[1:n-1]) + honeys[n//2]
else :
    # 짝수라면 중간값 2가지 중에 큰 것을 선택
    # 중간 값이 n //2 일 경우, n//2 - 1 일 경우 중 최댓값
    case2 = max(sum(honeys[1 : n//2]) + sum(honeys[n//2 -1 : n-2]) , 
                sum(honeys[1 : n//2+1] + sum(honeys[n//2 : n-2])) )

# case 3 벌통 ... 벌2 ... 벌1
case3 = 0
for bee2 in range(1,n-1) : # 벌2는 [1] ~ [-2]까지 가능
    b1 = sum(honeys[ : n-1]) - honeys[bee2] # 0부터 -2(n-2) 까지 가다가 벌2만 제거
    b2 = sum(honeys[ : bee2]) # 벌2는 [0] ~ [bee2 - 1]
    case3 = max(b1 + b2 , case3) # 더 큰값으로 갱신
    
print(case1, case2 , case3)
print(max(case1, case2, case3))

###########################################################################

# 시간 초과가 나는 이유 ? n 이 10만 이하 -> O(n * 2) (sum 때문에...)
# sum을 매번 계산하지 말고 저장해두기? 하나의 리스트로
sum_honeys = [honeys[0]]

for i in range(n-1): # 0 ~ n-2
    sum_honeys.append(sum_honeys[i]+honeys[i+1]) 

# case 1 벌1 ... 벌2 ... 벌통
case1 = 0
for bee2 in range(1,n-1) : # 벌2는 [1] ~ [n-2]까지 가능
    b1 = sum_honeys[n-1] - honeys[0] - honeys[bee2]  # 1부터 끝까지 가다가 벌2만 제거
    b2 = sum_honeys[n-1] - sum_honeys[bee2]
    case1 = max(b1 + b2 , case1) # 더 큰값으로 갱신

# case 2 벌1 ... 벌통 .. 벌2 
# -> 벌통이 딱 중간에 있지 않는 예외가 발생... 
case2 = 0
for middle in range(1, n-1): # 벌통은 [0] 과 [n-1]은 제외하고 가능
    ######################### 여기서 범위를 n-2로 해서 계속 틀렸다 범위 항상 주의하기!
    # 벌통이 중간에 있으면 벌을 제외하고 다 더하고 벌통을 한번 더 더해줌
    b1 = sum_honeys[middle] - honeys[0] 
    b2 = sum_honeys[n-2] - sum_honeys[middle -1] 
    case2 = max(b1 + b2, case2) 


# case 3 벌통 ... 벌2 ... 벌1
case3 = 0
for bee2 in range(1,n-1) : # 벌2는 [1] ~ [n-2]까지 가능
    b1 = sum_honeys[n-2] - honeys[bee2] 
    b2 = sum_honeys[bee2-1]
    case3 = max(b1 + b2 , case3) # 더 큰값으로 갱신


# print(case1, case2, case3)
print(max(case1, case2, case3))