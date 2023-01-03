# merge sort

def merge_sort(l):
    length = len(l)
    if length <= 1:
        return l
    half = length // 2
    first_list = merge_sort(l[:half])
    second_list = merge_sort(l[half:])
    result = []

    while first_list and second_list:
        if first_list[0] < second_list[0]:
            result.append(first_list.pop(0))
        else:
            result.append(second_list.pop(0))

    while first_list:
        result.append(first_list.pop(0))
    while second_list:
        result.append(second_list.pop(0))
    return result

input_list = input().split()
input_list = [int(i) for i in input_list]

print(merge_sort(input_list))