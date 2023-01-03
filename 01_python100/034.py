user_input = input()

l = list(map(int, user_input.strip().split()))
# l = [int (i) for i in l] # int가 아니면 ValueError

# print(l.sort()) 외않되?

# if l != sorted(l):
# 	print("NO")
# else:
# 	print("YES")