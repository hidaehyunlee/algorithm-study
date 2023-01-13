# 반드시 정렬할 모든 원소가 양수여야함
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(arr) + 1) # 가장 큰 값 + 1 크기의 리스트 선언

for i in range(len(arr)):
    count[arr[i]] += 1 # 각 데이터에 해당하는 인덱스값 +1

# 정렬된 값 출력
for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')