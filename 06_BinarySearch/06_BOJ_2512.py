# 시작점을 1, 끝점을 예산 요청 금액이 가장 큰 값으로 설정
# 중간점을 상한액으로 설정
# 예산 요청 금액이 상한액보다 크면 상한액을 배정하고, 작으면 요청 금액 그대로 배정한
# 시작점과 끝점이 같아지면 조건을 만족하는 상한액(즉, 배정된 예산의 최댓값)은 결국 (mid-1)한 끝점 값이 된다.

n = int(input())
arr = sorted(list(map(int, input().split())))
total = int(input())

start = 0
end = max(arr)

while start <= end:
    mid = (start+end) // 2
    result = 0

    for i in arr:
      if i > mid:
        result += mid
      else:
        result += i
    if result <= total: #총 금액보다 결과가 작으면 더 상한액을 높여서
      start = mid+1
    else:
      end = mid-1  

print(end)