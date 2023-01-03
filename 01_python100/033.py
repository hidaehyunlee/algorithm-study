n = input()
l = list(n.strip().split())

for i in range(len(l)-1, -1, -1): # 두번째 인자를 0으로 하면 인덱스0 포함 x
	print(l[i], end=' ')