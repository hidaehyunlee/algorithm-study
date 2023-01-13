arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)): # 0은 정렬되어있다고 가정
    for j in range(i, 0, -1): # i 부터 1까지 감소
        if arr[j] < arr[j - 1]: # 앞이 더 크면 한 칸씩 왼쪽으로 이동
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else: # 앞이 더 작으면 현재 위치에서 멈춤
            break

print(arr)