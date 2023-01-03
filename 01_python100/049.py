# 순서가 없는 10개의 숫자가 공백으로 구분되어 주어진다. 주어진 숫자들 중 최댓값을 반환하라.

l = sorted(list(map(int, input().split())), reverse=True)

print(l[0]) # 혹은 reverse 안하고 l[-1] !!!!!
