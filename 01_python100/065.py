'''
a = [1,2,3,4]
b = [a,b,c,d]
-> [[1,a],[b,2],[3,c],[d,4]] a,b리스트가 번갈아가면서 출력
'''

a = [1,2,3,4]
b = ['a','b','c','d']
new = list()

for i, j in zip(a, b):
    if (i + len(a)) % 2 != 0: # 5678
        new.append([i, j])
    else:
        new.append([j, i])

print(new)