
arr = list(map(str, input()))

arrInt = []
for c in arr:
    arrInt.append(ord(c))

n = len(arrInt)
result = [""] * n


# idea : 제일 낮은 문자를 찾고 그 뒤에 넣을 수 있는지 확인 -> 있다면 뒤에서 또 낮은 문자를 찾고 넣을 수 있는지 확인 -> 없다면 앞에서 가장 낮은 문자를 찾는다
# 재귀적으로 arr와 시작점을 기준으로 찾는다.

# 추가사항 : chr끼리도 min값을 찾을 수 있다고 한다. 나는 min을 쓰려고 Int로 바꾼건데 굳이 그러지 않아도 되는 것이었다.

def find(arr, start):
    if len(arr) == 0:  # 문자열이 모두 다 나옴(나오지 않은 문자가 없다)
        return

    minValue = min(arr)
    index = arr.index(minValue)  # 뒤에서 가장 낮은 문자의 위치를 찾음

    result[start + index] = chr(minValue)  # 대문자로 변환
    print("".join(result))

    find(arr[index+1:], start + index + 1)  # 뒷부분을 체크 (이게 우선적)
    find(arr[:index], start)  # 앞부분을 체크


find(arrInt, 0)
