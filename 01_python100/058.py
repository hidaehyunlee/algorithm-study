# 다시 풀기

# 숫자를 입력 받고 천단위로 콤마(,)를 찍어주세요.
# 예를들어, 123456789를 입력받았으면 123,456,789 를 출력해야합니다.

# s = str(input())
# won = list()
# k = 0

# for i in range(len(s) // 3):
#     tmp = s[-3 - k] + s[-2 - k] + s[-1 - k]
#     won.append(tmp)
#     k += 3

n = int(input())

result = format(n, ',') # 1000 단위 콤마(만 됨)
print(result)
