data = sorted(list(map(int, input().split())), reverse=True)
set_data = sorted(list(set(data)), reverse=True)
count = 0

if len(set_data) <= 3:
    count = len(data)
else:
    forth = set_data[3]

    for i in data:
        if i == forth:
            break
        else:
            count = count + 1

print(count)
# print(data)
# print(set_data)