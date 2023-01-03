# 1. 자료형
import imp
from os import remove


ia: int = 1000; # 정적 타입 선언 방법(기본적으토 타입 명시 안해줘도 됨)
'''
실수(float)
- double 없음
- 소수부, 정수부가 0일 때 0을 생략한다.
- e를 이용한 지수표현방식을 사용
    - e 다음에 오는 수는 10의 지수부(제곱)을 의미한다,
    - 1e9 == 10억 (10의 9제곱)
- round(실수, 반올림 할 소수점 자리수 - 1)의 활용
    - 실수 연산 시 정확히 표현하기 위해 소수점 다섯 번째 자리에서 반올림 해 계산하자.
'''
fa: float = 5.
fb = -.7 
fc = 42.25e1 #422.5
fd = 4225e-3 #4.225
print(fa, fb, fc, fd)

fr = 0.3 + 0.6 # 0.899999999... => a != 0.9
if round(fr, 4) == 0.9:  # 소수점 5번째 자리에서 반올림 했기 때문에 참
    print(True)
else:
    print(False)

# 거듭제곱 연산자
print(2 ** 10) # 1024 

# 나누기 연산자
'''
/ : 나누기
// : 몫
% : 나머지
'''

'''
iterable 자료형: list, tuple, dict, set
- Python의 모든 iterable 자료형은 각 요소의 데이터 타입이 자유롭다. 
    - 하나의 List에 정수, 실수, 문자열 등이 함께 들어갈 수 있다는 뜻.
'''

'''
리스트(list)
- c++의 벡터와 비슷
- 인덱싱: 음수를 넣으면 뒤에서부터 거꾸로 탐색 
    - list[-1] => 가장 마지막 원소
- 슬라이싱: 리스트에서 연속적인 값 가져올 때 사용. 콜론(:) 앞 뒤로 인덱스를 넣어줌
    - list[1 : 4] => 두 번째부터 네 번째 원소
    - 문자열(str)도 인덱싱과 슬라이싱 가능 (문자열은 immutable 자료형)

- 리스트 컴프리헨션: for문과 if문을 넣어 리스트 초기화하는 방법 
    - 특정 크기의 2차원리스트를 초기화할 때 반드시 사용해야함
- 기타 메서드
    - append() [O(1)], 
    - sort(), sort(reverse = True) [O(NlogN)], 
    - reverse(), insert(), remove(), count() [O(N)],  
'''
# 리스트 및 빈 리스트 선언
lst: list = [1, 2, 3, 4, 5]
empty_lst_1 = list()
empty_lst_2 = []

# 크기가 N(입력값)이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
la = [0] * n 

# 슬라이싱
s: str = "hello"
print(s[1 : 4]) # ell

# 리스트 컴프리헨션
odd_lst = [i for i in range(20) if i % 2 == 1] 
print(odd_lst) # [1, 3, 5, 7 ... 19]
pow_lst = [i * i for i in range(1, 10)] # range(1, 10) => 1 ~ 9
print(pow_lst) # [1, 4, 9, 16 ... 81]

# N*M 크기의 2차원 리스트 초기화 
n = 3
m = 4
lb = [[0] * m for _ in range(n)]
print(lb)

# 특정한 값의 원소 모두 제거
lst = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # [3, 5] 도 가능

result = [i for i in lst if i not in remove_set]
print(result) # [1, 2, 4]

'''
튜플(tuple) 
- 리스트와 비슷한데 딱 두 가지가 다르다.
    1. 한 번 선언된 값을 변경할 수 없다. (immutable)
    2. 소괄호를 사용해 초기화 한다.
'''
t: tuple = (1, 2, 3)
# t[0] = 100 => ERROR! 대입연산자로 값을 변경할 수 없다.

'''
사전(Dict)
- 내부적으로 hash table 사용해 검색/수정 O(1)
- 관련 함수 
    - keys(), values()
'''
dic = dict()
dic["사과"] = "apple"
dic["바나나"] = "banana"

if "사과" in dic:
    print(dic["사과"]) # value 출력 (apple)

# keys() 와 values(): 각각 키와 값 데이터만 뽑아서 리스트 형태로 return
key_lst = dic.keys()
value_lst = dic.values()
# 각 키에 따른 value들을 하나씩 출력
for k in key_lst:
    print(dic[k])

'''
집합(set)
- 중복 허용 X
    - s{1, 1, 1, 2, 3} => {1, 2, 3}
- 순서 X (indexing 불가능)
- 초기화 방법
    1. set([1, 2, 3])
    2. 중괄호 {}
- 연산자 (합집합(|), 교집합(&), 차집합(-))
- 기타 함수
    - add(e), remove(e)
    - update([e, e]): 새로운 원소 여러개 추가
'''
# 선언 및 초기화
s1 = set([1, 1, 1, 2, 3])
s2 = {1, 1, 1, 2, 3}
print(s1) # {1, 2, 3}
print(s2)

# 연산(합집합, 교집합, 차집합)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print(A | B) # {1,2,3,4,5,6,7}
print(A & B) # {4, 5}
print(A - B) # {1, 2, 3} => A와 B의 교집합을 A에서 뺀 부분

# 2. 조건문과 연산자
'''
- if ~ elif ~ else 문 사용
- : 다음 줄에 들여쓰기(스페이스바 4번) 으로 단락 구분
- 조건부 표현식: if ~ else 문을 한 줄에 사용
    - list의 원소 값을 변경해서 또다른 list를 만들 때 유용하게 사용.
    - 리스트 컴프리헨션 참고
- 일반 수학의 부등식 그대로 사용 가능 (논리 연산자 안써도 됨)
    - 0 > x & x < 20 ==> 0 < x < 20
'''
# 조건부 표현식
score = 85
result = "PASS" if score >= 90 else "FAIL"
print(result) # FAIL


# 연산자
'''
3.1. 비교 연산자: c와 같음
3.2. 논리 연산자
    - and, or, not 사용
3.3. in 연산자와 not in 연산자
    - 딕셔너리, 리스트, 문자열, 튜플 등 iterable 자료형에 사용 가능
'''

# 3. 반복문
scores = [90, 85, 50, 77, 97]
for i in range(5): # range 인자 하나면 0부터 시작 -> 인덱스 조회 활용
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다") # , 로 인자 여러개 출력

# 4.함수
'''
def name(parameter):
    ...
    return value

- global 키워드: 함수 안에서 global 키워드로 변수를 만들면 지역변수가 아니라 함수 바깥의 변수를 참조
'''
# global
g = 0
def addOne():
    global g
    g += 1 # g++ 이 안돼?

for _ in range(5):
    addOne()
print(g)


# 5. 입출력
'''
- 입력 구분이 줄바꿈/공백 일때 서로 다르게 처리해야함
- 줄바꿈: int(input()) 반복
- 공백: list(map(int, input().split()))
- 빠른 입력처리: 
    - import sys
      sys.stdin.readline().rstrip() 
'''
# 입력
# n = int(input()) # 입력받을 데이터 개수 입력
# data = list(map(int, input().split())) # 각 데이터를 공백으로 구분해 입력
# print(data)

# import sys
# data = sys.stdin.readline().rstrip() # rstrip() 은 엔터 제거해줌
# print(data) 

# 출력 3가지 방법
my_age = 26
print(f"제 나이는 {my_age}살 입니다") # f-string 문법: 문자열 앞에 접두사 f를 붙여야 함.
print("제 나이는", my_age, "살 입니다") # 인자 사이에 공백 삽입되어 출력 !!
print("제 나이는 " + str(my_age) + "살 입니다")

# 6. heap
'''
import heapq
- 최소힙
    - 최대힙을 제공 안하기 때문에 내림차순 정렬하려면 넣을때, 뺄때 원소 부호를 바꿔주면 된다.
- insert: heapq.heappush(queue, elem)
- removeMin: heapq.heappop(queue)
'''
# 힙정렬
import heapq
def heapsort(iterable):
    h = []
    res = []
    for e in iterable:
        heapq.heappush(h, e)
    for _ in range(len(h)):
        res.append(heapq.heappop(h))
    return res

res = heapsort([1, 3, 5, 7, 9, 2, 0, 4, 8, 6, 10])
print(res)

