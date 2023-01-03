def solution(l):
    l = sorted(l)
    for i in range(len(l) - 1):
        if l[i]+1 != l[i+1]:
            return 'NO'
    return 'YES'

input_list = list(map(int, input().split()))
#input_list = [int(i) for i in input_list]

print(solution(input_list))