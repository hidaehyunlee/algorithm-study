def solution(n, m):
    data = []
    min_val = 10000
    res = 0


    for i in range(n):
        data.append(list(map(int, input().split())))

        min_val = min(data[i])

        if res < min_val:
            res = min_val

    print(res)

n, m = map(int, input().split())
solution(n, m)

'''
행에서 가장 작은 값 저장
그 값을 res에 복사
그 다음행의 가장 작은 값을 res와 비교해서, res가 더 작으면 res = min_val
'''