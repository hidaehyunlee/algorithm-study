def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10)) # two 함수를 반환하기때문에 a가 two 함수가됨 -> 10은 one 함수 내부함수의 인자로 들어감 
print(b(10))
print(c(10))