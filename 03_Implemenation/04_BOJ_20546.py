# 기적의 매매법 https://www.acmicpc.net/problem/20546
# 메모: if stock_prices[i] < stock_prices[i - 1] < stock_prices[i - 2]: 이게 되네
'''
준현: 보유 현금이 주가보다 많으면 가능한만큼 매수. 매도 X
성민: 3가지 룰
    1. 전량 매수 전량 매도
    2. 주식이 3일째 상승하면 전량 매도 (동일 != 상승)
    3. 3일째 하락하면 전량 매수 (동일 != 하락)

14일간 거래, 14일째의 자산은 (현금 + 주식 수 * 1.14의 주가)
'''

jh = sm = int(input()) # 각각의 초기 자산
jh_stock = 0
sm_stock = 0
stock_prices = list(map(int, input().split()))

# 준현
for price in stock_prices:
    if jh >= price:
        jh_stock += (jh // price)
        jh %= price

jh += (jh_stock * stock_prices[-1])

# 성민
for i in range(2, len(stock_prices) - 1):
    # 매수 (3일연속 하락)
    if stock_prices[i] < stock_prices[i - 1] < stock_prices[i - 2]:
        if sm >= stock_prices[i]:
            sm_stock += (sm // stock_prices[i + 1])
            sm %= stock_prices[i + 1]

    # 매도 (3일 연속 상승)
    if stock_prices[i] > stock_prices[i - 1] > stock_prices[i - 2]:
        sm += (sm_stock * stock_prices[i + 1])
        sm_stock = 0

if jh > sm:
    print("BNP")
elif sm > jh:
    print("TIMING")
else:
    print("SAMESAME")