# 1. 반복문
def fac_iterative(n):
    res = 1
    # 1부터 n까지의 수를 치례대로 곱하기
    for i in range(1, n + 1):
        res *= i

    return res

# 2. 재귀
def fac_recursion(n):
    # 종료조건
    if n <= 1:
        return 1
    
    return n * fac_recursion(n - 1)