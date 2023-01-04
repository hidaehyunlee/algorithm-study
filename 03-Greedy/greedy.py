'''
탐욕법: 매 순간 가장 좋아보이는 것 선택, 현재의 선택이 나중에 미칠 영향 고려 x
    - 정렬 알고리즘이랑 주로 같이 출제됨
'''


'''
1. 거스름돈 문제 p87
    - 입력: 거스름돈 N은 항상 10의 배수
    - 출력: 거슬러 줄 동전의 최소 개수 (500/100/50/10원 존재)
'''
n = input(int())
coins = [500, 100, 50, 10]
cnt = 0

for coin in coins:
    cnt += n // coin
    n %= coin
print(cnt)

