
## 1. 그리디 Greedy

>  탐욕법: 현재 상황에서 지금 당장 좋은 것만 고르는 방법

- 가장 큰 순서대로, 가장 작은 순서대로 등의 기준 제시 
  - 보통 정렬 알고리즘과 짝을 이뤄 출제



## 2. 구현 Implemetaion

> 구현: 머리속에 있는 알고리즘을 소스코드로 바꾸는 과정

- 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
  - 문법, 라이브러리에 익숙치 않을 때, 조건이 까다로울 때
- 완전탐색, 시뮬레이션 유형



## 3. 자료구조 Data Structure

- `push` , `pop` : 스택과 큐의 핵심함수
- overflow와 underflow를 고려해야함

### 3.1. Stack

- FILO: 선입후출
  - 박스(그릇) 쌓기에 비유. 아래서 위로 쌓고, 위에서부터 내림
- 별도 라이브러리 없이 `list` 활용

```python
stack = []

# push
stack.append(1)
stack.append(2) 
stack.append('a')
print(stack) 

# pop
stack.pop()
print(stack)

# print top
print(stack[-1])
```



### 3.2. Queue

- FIFO: 선입선출

  - 대기줄에 비유. 먼저 온 사람이 먼저 처리.
  - '공정한' 자료구조

- 큐 구현을 위해 deque 라이브러리 사용

  ```python
  from collections import deque
  ```

  - `deque`: 스택과 큐의 장점 모두 취한 자료구조
    - pop()을 통해 top을 제거할 수도 있고, 
    - pushleft()를 통해 제일 밑에 넣을수도 있음
  - 다시 list 자료형으로 변환 가능

```python
from collections import deque

queue = deque()

# push
queue.append(1)
queue.append(2)
queue.append(3)
print(queue) # deque([1, 2, 3])

# pop (첫 번째 요소)
queue.popleft() 
print(queue) # deque([2, 3])

# push bottom
queue.appendleft(0)
print(queue) # deque([0, 2, 3])
```



### 3.3. 재귀 Recursion

- 함수는 스택 메모리에 적재. 
  - 즉, 재귀함수는 내부적으로 스택 자료구조와 동일
  - 따라서 DFS 등 스택을 활용해야하는 알고리즘은 재귀 함수를 이용해 간편하게 구현할 수 있다. 



### 3.4. 그래프

- 탐색이 복잡하지만 메모리를 효율적으로 활용



## 4. 탐색 DFS/BFS

> 탐색: 많은 양의 테이터 중에서 원하는 데이터를 찾는 과정

- 그래프, 트리 등의 자료구조 안에서 DFS, BFS 알고리즘 사용

### 4.0. 그래프 표현 방식

1. **인접 행렬:** 2차원 배열에 각 노드가 연결된 형태를 기록. 연결된 노드끼리의 간선 값을 적고, 연결되어 있지 않으면 999999999 등의 무한의 비용이라고 작성한다. 

   ```python
   INF = 999999999
   
   gragh = [
     [0, 7, 5],
     [7, 0, INF],
     [5, INF, 0]
   ]
   ```

   - 두 노드가 연결되어 있는지 확인할 때 유용. 노드 1과 노드 7이 연결되어 있는지 보려면 `g[1][7]` 만 확인하면 된다.

   ```python
   # 1. 그래프를 True False로 저장
   g = [[False] * (n + 1) for _ in range(n + 1)]
   for _ in range(m):
       a, b = map(int, input().split())
       g[a][b] = g[b][a] = True
   ```

   ```python
   4 5 1 # v, e, start
   1 2
   1 3
   1 4
   2 4
   3 4
   
   [[False, False, False, False, False], [False, False, True, True, True], [False, True, False, False, True], [False, True, False, False, True], [False, True, True, True, False]]
   ```

   

2. **인접 리스트:** 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결해 저장.

   - 딕셔러니 자료형으로 표현한다면, key는 출발 노드, value는 도착노드(리스트 형태) 가 된다.

   ```python
   # 행(row)이 3개인 2차원 리스트 선언
   gragh = [[] for _ in range(3)]
   
   # 각 노드0,1,2에 연결된 노드 정보 저장(버텍스, 엣지)
   gragh[0].append((1, 7))
   gragh[0].append((2, 5))
   
   gragh[1].append((0, 7))
   
   gragh[2].append((0, 5))
   ```

   ```python
   [[(1, 7), (2, 5)], [0, 7], [1, 5]]
   ```

   - 특정 노드와 연결된 모든 인접 노드를 순회할 때 유용.

### 4.1. DFS

> 깊이 우선 탐색: 그래프에서 깊은 부분을 우선적으로 탐색

- 백트래킹: 탐색을 하다가 더 갈 수 없으면 왔던 길을 되돌아가 다른 정답을 찾는 알고리즘

  - 가보고 되돌아오고를 반복, 가능성이 없으면 즉시 후보를 포기한다는 것이 중요.

  - 제약충족문제(CSP, Constraint Satisfaction Problems)

- 스택 자료구조에서의 동작 과정

  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
  2. 스택 top에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리
     - 방문하지 않은 인접 노드가 없으면 top pop
  3. 1, 2번 반복

- 스택 즉, 재귀를 활용하면 간단

  ```python
  def dfs(v, visited =[]):
    visited.append(v)
    for i in graph[v]:
      if not i in visited:
      	visited = dfs(i, visited)
    return visited
  ```

  

### 4.2. BFS

> 가까운 노드부터 탐색

- 그래프의 최단경로 찾는 문제에서 사용 

- 큐 자료구조를 사용: 인접노드를 반복적으로 큐에 넣으면, 자연스럽에 먼저들어온 것이 먼저 나가게 됨
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
  2. 큐에서 노드를 꺼내(popleft), 해당 노드의 인접노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
  3. 1,2번 반복



## 5. 정렬

- 데이터 정렬 후 이진 탐색 가능

### 5.1. 선택정렬

> 가장 작은 데이터를 선택에 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복 -> 매번 가장 작은 것을 선택

- `n - 1` 번 반복하면 정렬 완료

- `O(n^2)`
- 매우 비효율적. 그래도 특정 리스트에서 가장 작은 데이터를 찾는 형태는 익숙해지기.



### 5.2. 삽입정렬

- 개념
  1. 첫번째 데이터는 그 자체로 정렬되어있다고 가정하고, 두번째 데이터부터 **역순으로 확인**
  2. 두번째 데이터가 앞의 데이터보다 큰지 작은지만 판단에서 왼쪽 혹은 오른쪽으로 들어가는 두 경우만 존재
  3. 세번째 데이터는 마찬가지로 3가지 경우만 존재, 특정 데이터 사이로 '삽입'될 수 있음
- 특징: 정렬 중간에도, 항상 오름차순을 유지하고 있음.
  - 즉, 삽입 위치 == 삽입될 데이터보다 작은 데이터를 만난 위치
  - **앞의 데이터와 비교해서 현재 데이터가 더 작으면 앞과 swap, 앞이 더 크면 break**
  - 그 앞까지 확인할 필요 없음
- 데이터가 거의 정렬되어 있는 경우 다른 정렬보다 빠름

> **range(start, end, step)**
>
> 세 번째 매개변수인 step에 -1이 들어가면, start부터 end + 1 까지 -1씩 감소한다.



### 5.3. 퀵정렬

- 가장 많이 사용
- 기준(`pivot`)을 설정한 다음, 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식

##### 호어 분할(Hoare Partition) 방식

> 리스트에서 **첫 번째 데이터를 피벗**으로 정한다.

1. **파트 1**
   1. 왼쪽에서는 피벗보다 큰 데이터를 찾고, 오른쪽에서는 피벗보다 작은 데이터를 찾는다. 
      - 이때 왼쪽은 피벗의 왼쪽이 아니라 나머지 리스트에서의 제일 왼쪽
      - **만약 두 값이 엇갈린 경우(작은게 왼쪽, 큰게 오른쪽이 된 경우) 피벗과 작은 값의 위치를 서로 변경한다.**
   2. 그리고 교환
   3. 1, 2의 반복
2. 파트 2
   1. 분할: 이제 피벗 왼쪽의 데이터는 모두 피벗보다 작고, 오른쪽 리스트는 모두 피벗보다 큰 값들이다.
   2. 두 리스트에 대해 각각 피벗을 설정해 똑같은 방법으로 정렬을 수행한다.

- 파트2에서 피벗 양쪽 리스트에 대해 같은 과정을 반복하기 때문에, **재귀로 구현하면 간결**해짐
- 종료조건: **현재 리스트의 데이터 개수가 1개인 경우**
  - 분할이 불가능 -> 정렬 완료



##### List Comprehension: 리스트 안에서 for문, if문 사용

```python
[ 출력식 for 원소 in 리스트 if문 ]
new_list = [ i for i in og_list if i >= 5]
```

```python
# 1~10까지 숫자 중에 5이상만 list로 저장
og_list=[1,2,3,4,5,6,7,8,9,10]
new_list = []

for i in og_list :
    if i >= 5  :
        new_list.append(i)


##### result #####   
[5, 6, 7, 8, 9, 10]
```

위와 아래가 같음



### 5.4. 계수 정렬 count sort

- 데이터 크기 범위가 제한되고, 정수일때만 사용 가능
  - 왜냐면 모든 데이터(범위)를 담을 수 있는 크기의 리스트를 선언해야하기 때문
  - 일반적으로 가장 큰 데이터와 작은 데이터 차이가 1000000 이하일 때 효과적
    - 이 경우 10000001 * int 크기의 리스트 선언

- 데이터의 개수가 N, 데이터 중 최댓값이 K일 때 O(N + K)
- **새 리스트의 인덱스의 값 == 인덱스 숫자 데이터의 개수**
  - **즉, 이 새 리스트에 저장된 데이터 자체가 정렬된 형태**
  - **리스트의 첫 번째 데이터부터 하나씩 그 값만큼 인덱스를 출력하면 된다.**



### 5.5. sorted 와 sort

```python
new = sorted(arr) # 새 리스트 반환
arr.sort() # 내부 원소 정렬
```

```python
'''
리스트의 데이터가 튜플로 구성되어 있을 때,
각 데이터의 두 번째 데이터로 정렬
'''

arr = [('대리', 2), ('히리', 5), ('태리', 3)]

def setting(data):
    return data[1]

res = sorted(arr, key=setting)
print(res)
```



## 6. 이진탐색 Binary Search

> 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 찾는 과정

- 조건: 리스트가 정렬된 상태

  1. 위치를 나타내는 변수(인덱스)를 3개 사용 (start, end, mid)

  2. 찾으려는 데이터가 mid 보다 작으면, mid 이전의 값만 확인한다.

     즉, end를 mid - 1로 옮긴다. 큰 경우에도 같은 원리.

  3. 위 과정을 반복해, 한 단계를 거칠때마다 확인하는 원소가 평균적으로 절반으로 줄어든다. 

     -> O(logN)의 시작복잡도를 가진다.

- 구현은 재귀 혹은 반복문을 이용한다.

- 종료 조건: `start > end`

- 이진 탐색 트리:
  - **left child < parent < right chile** 가 항상 성립하는 트리 자료구조



### 6.1. 문제 모음

| 순번 | 추천 문제 | 문제 번호                                      | 문제 이름                                                    |
| ---- | --------- | ---------------------------------------------- | ------------------------------------------------------------ |
| 00   | ✔️         | [1789](https://www.acmicpc.net/problem/1789)   | [수들의 합](https://www.acmicpc.net/problem/1789)            |
| 01   | ✔️         | [10815](https://www.acmicpc.net/problem/10815) | [숫자 카드](https://www.acmicpc.net/problem/10815)           |
| 02   | ✔️         | [2417](https://www.acmicpc.net/problem/2417)   | [정수 제곱근](https://www.acmicpc.net/problem/2417)          |
| 03   | ✔️         | [2512](https://www.acmicpc.net/problem/2512)   | [예산](https://www.acmicpc.net/problem/2512)                 |
| 04   | ✔️         | [19637](https://www.acmicpc.net/problem/19637) | [IF문 좀 대신 써줘](https://www.acmicpc.net/problem/19637)   |
| 05   | ✔️         | [11663](https://www.acmicpc.net/problem/11663) | [선분 위의 점](https://www.acmicpc.net/problem/11663)        |
| 06   | ✔️         | [2805](https://www.acmicpc.net/problem/2805)   | [나무 자르기](https://www.acmicpc.net/problem/2805)          |
| 07   | ✔️         | [1654](https://www.acmicpc.net/problem/1654)   | [랜선 자르기](https://www.acmicpc.net/problem/1654)          |
| 08   | ✔️         | [22871](https://www.acmicpc.net/problem/22871) | [징검다리 건너기 (large)](https://www.acmicpc.net/problem/22871) |
| 09   | ✔️         | [3079](https://www.acmicpc.net/problem/3079)   | [입국심사](https://www.acmicpc.net/problem/3079)             |
| 10   | ✔️         | [2470](https://www.acmicpc.net/problem/2470)   | [두 용액](https://www.acmicpc.net/problem/2470)              |
| 11   | ✔️         | [20444](https://www.acmicpc.net/problem/20444) | [색종이와 가위](https://www.acmicpc.net/problem/20444)       |
| 12   | ✔️         | [2110](https://www.acmicpc.net/problem/2110)   | [공유기 설치](https://www.acmicpc.net/problem/2110)          |
| 13   | ✔️         | [1477](https://www.acmicpc.net/problem/1477)   | [휴게소 세우기](https://www.acmicpc.net/problem/1477)        |
| 14   | ✔️         | [13397](https://www.acmicpc.net/problem/13397) | [구간 나누기 2](https://www.acmicpc.net/problem/13397)       |
| 15   | ✔️         | [2412](https://www.acmicpc.net/problem/2412)   | [암벽 등반](https://www.acmicpc.net/problem/2412)            |
| 16   | ✔️         | [1939](https://www.acmicpc.net/problem/1939)   | [중량제한](https://www.acmicpc.net/problem/1939)             |
| 17   | ✔️         | [2473](https://www.acmicpc.net/problem/2473)   | [세 용액](https://www.acmicpc.net/problem/2473)              |
| 18   | ✔️         | [1300](https://www.acmicpc.net/problem/1300)   | [K번째 수](https://www.acmicpc.net/problem/1300)             |
| 19   | ✔️         | [7453](https://www.acmicpc.net/problem/7453)   | [합이 0인 네 정수](https://www.acmicpc.net/problem/7453)     |



## 7. DP

> 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법
>
> - 분할 정복과의 차이는 작은 문제들이 서로 영향을 미치고 있다는 점

- DP 사용 조건

  1. 큰 문제를 작은 문제로 나눌 수 있다
  2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다

- 종류

  - 탑다운(메모제이션): 재귀를 이용. 큰 문제를 해결하기 위해 작은 문제를 호출
    - 맨 위 값에서 재귀로 제일 작은 인덱스를 향하는 것

  - 바텀업: 반복문 이용. 작은 문제부터 답을 도출
    - 제일 작은 인덱스에서 목표하는 값으로 향하는 것 
    - **처음 두 수를 알 때 활용**

- DP 테이블: 바텀업 방식에서 사용되는 결과 저장용 리스트

- **`d[0]` 과 `d[1]` 경우의 값 구하고 점화식 세워서 d[n] 일때까지 반복**



## 8. 최단경로

> 길 찾기 문제. 그리디와 DP 알고리즘이 적용됨

- 한 지점 -> 특정 지점
- 모든 지점 -> 다른 모든 지점

### 8.1. 다익스트라(Dijkstra) 최단 경로

> 그래프에서 여러 노드가 있을 때, **특정 노드에서 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘** 

- 음의 간선이 없을 때 동작 -> 현실 GPS 소프트웨어 알고리즘
- 최단거리 테이블: *각 노드에 대한 현재까지의 최단거리* 정보를 담은 1차원 리스트
- 그리디 알고리즘으로 분류: 매번 **'가장 비용이 적은 노드'**를 선택해서 임의의 과정을 반복하기 때문
  1. 출발 노드를 설정
  2. 최단거리 테이블 초기화 (무한, 999999999, `int(1e9) -> 10억`)
  3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택
     - 즉, 테이블에 저장된 거리 중 가작 작은 간선값의 노드
     - 최단거리가 같다면 번호가 작은 노드 선택
  4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블 갱신
     - 인접한 간선을 하나씩 확인
     - **기존 테이블 값보다 작으면 갱신** -> 기준 노드를 거쳐서 가는 경우가 비용이 더 작으면 갱신
  5. 3번과 4번을 반복
- 테이블이 완성되면, 각 인덱스의 값은 출발 노드로부터 각 노드(index)까지 가기위한 최단 경로라는 뜻이다.



#### 1) 간단한 다익스트라 알고리즘

> 단계마다 *방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택*하기 위해 매 단계마다 1차원리스트의 모든 원소를 순차탐색 한다.

- O(v^2) , v는 노드의 개수
- 리스트를 v + 1의 크기로 할당해 노드의 번호를 index로 맞춘다.

- 노드의 개수가 10,000개를 넘어가면 이 코드로 해결 불가능



#### 2) 개선된 다익스트라 알고리즘

> *3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택*  할 때 리스트를 순차탐색 하지 않고 **heap 자료구조를 사용해 선형시간을 로그시간으로** 줄인다.

- Heap 자료구조: 우선순위 큐를 구현할 때 사용

  - 우선순위 값은 정수로 표현 -> `(가치, 정보)` 로 묶어서 우선순위 큐에 삽입

  - 대부분 언어의 우선순위큐 라이브러리에서는 **데이터의 묶음(튜플)을 넣으면 첫번째 원소를 기준으로 우선순위를 설정**한다.

  - 다익스트라에서는 최소 힙(값이 낮은 데이터가 먼저 삭제)기반의 `heapq`를 사용 

    > 메모: 만약 최대힙을 사용하고 싶다면 우선순위 값에 음수 부호(`-`) 를 붙인뒤 꺼낸 다음에 다시 음수 기호를 붙여서 원래의 값으로 돌리는 방식을 사용하면 된다.

- 즉, 최단거리 테이블(1차원 리스트)는 그대로 사용하고, **현재 가장 가까운 노드를 저장하기 위한 목적으로만 heapq를 추가로 사용**하는 개념

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 수, 간선 수
start = int(input()) # 시작 노드 번호
graph = [[] for _ in range(n + 1)] # 각 노드에 연결되어 있는 (노드, 비용) 리스트
distance = [INF] * (n + 1) # 최단거리 테이블

# 모든 간선 정보 입력 받기
for _ in range(m):
    # a노드에서 b노드로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # start 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 최단거리가 가장 짧은 노드 찾기 -> get_smallest_node() 와 같은 역할
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 현재 노드 now가 이미 처리된 적 있다면 무시
            continue
        
        # 현재 노드와 연결된 다른 인접 노드들 확인 -> 현재 노드를 거치는 비용이 더 적다면 업데이트
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 수행
dijkstra(start)

# start에서 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
```

```python
# input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

# output
0
2
3
1
2
4
```

```python
# graph의 생김새
    [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

# 각 단계별 distace[]의 생김새 (실제로는 10억이지만 길어져서 INF로 표기)
    [INF, 0, INF, INF, INF, INF, INF]
    [INF, 0, 2, INF, INF, INF, INF]
    [INF, 0, 2, 5, INF, INF, INF]
    [INF, 0, 2, 5, 1, INF, INF]
    [INF, 0, 2, 4, 1, INF, INF]
    [INF, 0, 2, 4, 1, 2, INF]
    [INF, 0, 2, 4, 1, 2, INF]
    [INF, 0, 2, 4, 1, 2, INF]
    [INF, 0, 2, 3, 1, 2, INF]
    [INF, 0, 2, 3, 1, 2, 4]
    [INF, 0, 2, 3, 1, 2, 4]
```



### 8.2. 플로이드 워셜 알고리즘

> **모든 지점에서 다른 모든 지점까지의 최단경로**를 구하는 알고리즘

- 다익스트라와는 다르게, 단계마다 방문하지 않은 노드중 최단거리를 갖는 노드를 찾지 않는다.

- 2차원 리스트에 '최단거리 정보'를 저장

- 알고리즘 (시간 복잡도는 O(*N^3*))

  1. 현재 확인하고 있는 노드를 제외하고, `n - 1` 개의 노드 중에서 서로 다른 노드 `(A, B)`쌍 을 선택한다.
  2. 이후 `A -> 1번 노드 -> B` 로 가는 비용을 확인한 뒤 최단 거리를 갱신한다.
  3. 3중 반복문을 사용해 k번(각 노드)의 단계를 반복한다.

- 즉, ***A에서 B로 가는 최소 비용***과 ***A에서 K를 거쳐 B로 가는 비용***을 비교해 더 작은 값으로 갱신

  - 초기 테이블

    | 출발\도착 | 1번  | 2번  | 3번  | 4번  |
    | --------- | ---- | ---- | ---- | ---- |
    | 1번       | 0    | 4    | INF  | 6    |
    | 2번       | 3    | 0    | 7    | INF  |
    | 3번       | 5    | INF  | 0    | 4    |
    | 4번       | INF  | INF  | 2    | 0    |

    - ex) 1번 노드부터 시작해 4번 노드까지 총 4 step
      1. *D32 = min(D32, D31 + D12)* = **INF -> 9**
      2. ~~D32 = min(D32, D32 + D22) = INF -> 9~~
      3. *D32 = min(D32, D33 + D32)* = **9**
      4. *D32 = min(D32, D34 + D42)* = **9 -> 9**
    - 위는 각 단계에서 자기 노드를 거쳐가는 계산(자기 노드를 제외하고 모든 경로를 구하는)이 어떻게 구해지는지에 대한 예시이고, 실제로는 각 단계에서 값이 바뀔 수 있음. 이 예시에서는 그대로임.

  - 4 step 후 테이블

    | 출발\도착 | 1번  | 2번  | 3번  | 4번  |
    | --------- | ---- | ---- | ---- | ---- |
    | 1번       | 0    | 4    | 8    | 6    |
    | 2번       | 3    | 0    | 7    | 9    |
    | 3번       | 5    | 9    | 0    | 4    |
    | 4번       | 7    | 11   | 2    | 0    |


