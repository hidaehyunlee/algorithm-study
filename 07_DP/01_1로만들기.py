# p.217 1로 만들기

# 두번째 풀이
# 점화식: 각 4개의 연산이 최소가 되면됨
x = int(input())
d = [0] * 30001

for i in range(2, x + 1):
    # 1을 빼고 시작하는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문
    d[i] = d[i - 1] + 1 # + 1은 cnt용
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1) # 여기서 d[x]의 값이 교체됨 
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    
print(d[x])

# n = int(input())
# d = [0] * 30001

# # bottom-up (loop)
# for i in range(2, n + 1):
#     d[i] = d[i - 1] + 1
    
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

# print(d[n])

