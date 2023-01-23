# p.201 -> Parametric Search 문제: 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 문제: 적어도 m만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값 구하기
# input: 
    # 떡의 개수 n, 요청한 떡의 길이 m | 4 6
    # 각 떡의 높이 | 19 15 10 17
# output: 15

# 첫 풀이: 19 17 15 10 내림차순 정렬 후, 인덱스0 값 -- 하며 m과 같을때까지 잘라보기
# 수정: 탐색범위가 10억이라, 1씩 내리는 순차탐색하면 타임오버. 이진탐색으로 높이 h를 줄여나가야함
#       떡의 길이 합이 m보다 크거나 같을때마다 정답을 mid 값으로 갱신해주면 됨

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
ans = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in arr:
        if i > mid:
            total += i - mid
    
    if total < m: # 떡 양이 부족하면 더 자르기 (왼쪽 부분 탐색)
        end = mid - 1
    else: # 덜 자르기
        ans = mid # 덜 잘랐을때가 정답이므로 여기에서 기록
        # print(ans, end=' ')
        start = mid + 1

print(ans)