arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    # 종료조건: 리스트가 하나의 원소만 가지고 있을때
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1::]

    # [ 출력식 for 원소 in 리스트 if문 ]
    left = [x for x in tail if x <= pivot] # 분할된 왼쪽
    right = [x for x in tail if x > pivot] # 분할된 오른쪽

    # 왼쪽 오른쪽 각각 정렬수행, 전체 리스트 반환
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(arr))