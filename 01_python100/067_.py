'''
- 악수는 모두 1대 1로 진행이 된다.
- 민규를 제외한 모든 참가자는 자신을 제외한 참가자와 모두 한번씩 악수를 한다.
- 같은 상대와 중복된 악수는 카운트 하지 않는다.
- 민규를 제외한 참가자는 행사를 모두 마쳤다.

input : n (행사에서 진행된 악수 횟수)
output : [민규의 악수횟수 , 행사참가자]
'''

# 1 2 : 1
# 1 2 3 : 3
# 1 2 3 4 : 6
# 1 2 3 4 5 : 10
# 59 -> [4, 12]

def solition(n):
    sum = 0
    handshake = 0
    people = 0

    for i in range(1, n + 2):
        sum += i
        # if sum == n:
        #     print(i)
        #     people = i + 1
        #     handshake = i
        if sum > n:
            print("yyyyyyy")
            people = i + 1  # sum = 66, i = 11
            prev_sum = sum - i
            handshake = n - prev_sum
            break;

    res = [handshake, people]
    print(res)

n = int(input())

solition(n)