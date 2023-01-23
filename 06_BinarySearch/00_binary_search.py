arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] # 10개

# 1. 재귀함수로 구현
def binary_search_recursion(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target: # 타겟보다 중간점이 크면, 왼쪽만 확인
        return binary_search_recursion(arr, target, start, mid - 1)
    else:
        return binary_search_recursion(arr, target, mid + 1, end)

# 2. 반복문으로 구현
def binary_search_loop(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target: # 타겟보다 중간점이 크면, 왼쪽만 확인
            end = mid - 1
        else:
            start = mid + 1
    
    return None

# test
print("재귀", binary_search_recursion(arr, 7, 0, len(arr) - 1))
print("루프", binary_search_loop(arr, 7, 0, len(arr) - 1))