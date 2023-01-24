import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))
ans = []

def binary_search(arr, target, n):
    start = 0
    end = n - 1
    key = '0'
    
    while start <= end:  
        mid = (start+end)//2  
        if target == arr[mid]:
            key = '1'
            break
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return key

for target in m_list:
    ans.append(binary_search(n_list, target, n))
print(' '.join(ans))