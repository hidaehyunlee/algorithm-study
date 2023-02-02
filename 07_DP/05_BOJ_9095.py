# 1,2,3 더하기 https://www.acmicpc.net/problem/9095
'''
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수 구하기
수를 1개 이상 사용해야함
'''

# 점화식: n이 3보다 클때, f(n) = f(n-3) + f(n-2) + f(n-1)
tc = int(input())

d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4 # 111, 12, 21, 3

while(tc):
    n = int(input())

    for i in range(4, n + 1):
        d[i] = d[i - 3] + d[i - 2] + d[i - 1]

    print(d[n])

    tc -= 1