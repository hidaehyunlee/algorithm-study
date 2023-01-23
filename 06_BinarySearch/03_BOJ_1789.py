# 수들의 합 https://www.acmicpc.net/problem/1789
# 서로 다른 N개의 자연수의 합이 S라고 한다. 
# S를 알 때, 자연수 N의 최댓값은 얼마일까?
# 풀이: 1부터 n의 총합이 s보다 같거나 작을동안 n++. 더 커진 idx의 e가 정답
# 단 이분탐색으로 풀기 -> 1부터 mid 합이 s보다 작거나 같은 동안, ans를 mid로 저장, 탐색

s = int(input())
start = 1
end = s
ans = 0

while start <= end:
    mid = (start + end) // 2

    if mid * (mid + 1) // 2 <= s:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
