def solution(n, m, k):
    limit = 0
    res = 0

    arr = list(map(int, input().split())) # 2 4 5 4 6

    for i in range(m):
        if limit != k:
            res += sorted(arr, reverse=True)[0]
            limit += 1
        else:
            res += sorted(arr, reverse=True)[1]
            limit = 0

    print(res)

n, m, k = map(int, input().split())
solution(n, m, k)

'''
m 번 돌면서
배열의 가장 큰수를 최대 k번 더함
그 다름 인덱스를 한번 더함
다시 가장 큰수를 최대 k번 더함
'''