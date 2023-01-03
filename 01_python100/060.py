#  enumerate(): '파이썬답게' 인덱스와 원소를 동시에 접근하면서 루프
'''
enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 tuple을 만들어줍니다. 
따라서 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 인자 풀기(unpacking)를 해줘야 합니다.
>>> for i, letter in enumerate(['A', 'B', 'C']):
...     print(i, letter)
...
0 A
1 B
2 C
'''

student = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']

# num = []
# name = []

for num, name in enumerate(sorted(student)):
    print(f"번호: {num + 1}, 이름: {name}")