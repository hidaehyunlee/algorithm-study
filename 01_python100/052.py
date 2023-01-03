# quick_sort

def quick_sort(l):
    length = len(l)
    if length <= 1:
        return l
    half_value = l.pop(length//2)
    first_list = []
    second_list = []
    
    for i in range(length-1):
        if l[i] < half_value:
            first_list.append(l[i])
        else:
            second_list.append(l[i])
    return quick_sort(first_list) + [half_value] + quick_sort(second_list)

input_l = input().split(' ')
input_l = [int(i) for i in input_l]

print(quick_sort(input_l))