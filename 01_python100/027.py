'''
딕셔너리 = dict(키1=값1, 키2=값2)
딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
딕셔너리 = dict([(키1, 값1), (키2, 값2)])
딕셔너리 = dict({키1: 값1, 키2: 값2})
'''

k = input().split()
v = map(int, input().split())

data = dict(zip(k, v))
print(data)