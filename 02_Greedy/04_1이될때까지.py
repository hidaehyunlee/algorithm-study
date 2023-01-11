'''
n과 k가 주어질 때, n이 1이 될때까지 아래 두 연산 중 하나 수행. 최소 횟수를 구하기
    n에서 1을 빼기
    n을 k로 나누기 (나누어 떨어질때만)
'''

n, k = map(int, input().split())
res = 0

while n >= k:
    while n % k != 0:
        n -= 1
        res += 1

    n //= k
    res += 1

while n > 1:
    n -= 1
    res += 1

print(res)

'''
25 3
6
'''