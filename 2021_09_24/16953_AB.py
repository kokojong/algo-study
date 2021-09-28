a, b = map(int, input().split())

cnt = 1

# 애초에 나누어 떨어지는것으로 분류할 필요가 없다.(어차피 포함된다..)

# 아이디어 : b를 2로 나누거나 맨 뒤에 1을 없애는 식으로 해서 찾아가기
while True:
    if b % 2 == 0:
        b = b / 2
        cnt += 1
    else:
        b -= 1
        b = b / 10
        # b = b // 10 도 될거라고 생각했지만 왜 안되는지 모르겠네요
        # https://www.acmicpc.net/board/view/69275 를 참고해서 왜 안되는지 알았습니다
        cnt += 1
    if b <= a:
        break

if b < a:
    print(-1)
else:
    print(cnt)

# 아래에는 시행착오입니다.. 하다가 깨달았습니다^^...

# if b % a == 0:
#     # 나누어 떨어진다면
#     c = b//a

# 이부분에서 오류가 발생
# (2 162 의 경우 c = 81인데 else문에도 while을 추가해주면 동일하게 동작)

#     if c % 10 in (3, 5, 6, 7, 9, 0):
#         print(-1)
#     else:
#         while c % 2 == 0:
#             c = c//2
#             cnt += 1
#         print(cnt)

# else:  # 애초에 안나눠지는거면
#     if b % 10 in (3, 5, 6, 7, 9, 0):
#         print(-1)
#     else:
#         while True:
#             if b % 2 == 0:
#                 a /= 2
#                 cnt += 1
#             else:
#                 b -= 1
#                 b /= 10
#                 cnt += 1
#             if b <= a:
#                 break
#         if b < a:
#             print(-1)
#         else:
#             print(cnt)
