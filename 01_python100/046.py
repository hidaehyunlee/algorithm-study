s = str()
res = 0

for i in range(1, 101):
    s += str(i)

s_int = map(int, s)
for i in s_int:
    res += i

print(res)