'''
리스트의 데이터가 튜플로 구성되어 있을 때,
각 데이터의 두 번째 데이터로 정렬
'''

arr = [('대리', 2), ('히리', 5), ('태리', 3)]

def setting(data):
    return data[1]

res = sorted(arr, key=setting)
print(res)