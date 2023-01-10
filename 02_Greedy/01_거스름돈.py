def solution(n):
    change = [500, 100, 50, 10]
    count = 0

    for coin in change:
        count += n // coin
        n %= coin

    print(count)

n = int(input())
solution(n)
 
    