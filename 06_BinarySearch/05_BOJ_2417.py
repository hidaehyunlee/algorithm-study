# 정수 제곱근 https://www.acmicpc.net/problem/2417
# q2 ≥ n인 가장 작은 음이 아닌 정수 q를 출력

# 두번째 풀이
# mid를 제곱해서 비교. 더 작으면 start를 높여나가며 비교
n = int(input())
start = 0
end = n

ans = 0
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        ans = mid # 더 클때가 정답이므로 여기서 기록
        end = mid - 1

print(ans)


# 1. 시작점, 끝점은 0과 n
# 2. 시작점과 끝점을 통해 중간 지점을 구하고
# 3. 중간 지점의 제곱 값과 n을 비교
# 4. 비교했을 때, n 미만이면 시작점 = 중간점 + 1
# 5. n 이상이면 끝점 = 중간점 - 1

# n = int(input())

# start = 0
# end = n

# while start <= end:
#     mid = (start + end) // 2
#     if mid ** 2 < n:
#         start = mid + 1
#     else:
#         end = mid - 1

# print(start)