# input().split(): 값 여러개 입력 받아 list에 저장
# map: int로 변환

score = list(map(int, input().split()))

print(int(sum(score) / len(score)))