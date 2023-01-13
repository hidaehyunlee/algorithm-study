n = int(input())

students = []
for _ in range(n):
    a, b = input().split()
    students.append((a, b))

def setting(data):
    return data[1]
res = sorted(students, key=setting)

# lamda
# res = sorted(students, key=lambda data: data[1])

for name, score in res:
    print(name, end=' ')