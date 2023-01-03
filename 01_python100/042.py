# 예를 들어 a = 5, b = 24라면 2020년 5월 24일은 일요일이므로 문자열 "SUN"를 반환하세요.

import datetime
from datetime import date

def solution(m, d):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    days_idx = datetime.date(2020, m, d).weekday()

    print(days[days_idx])

m = int(input())
d = int(input())

solution(m, d)


# date = datetime.datetime.today()
# print(date)
# date.year
# date.month
# date.day
# date.hour
# date.minute
# date.second
# date.microsecond

# print(datetime.date(2021, 8, 28))
# datetime.date.today()

# datetime.date(2021, 9, 28) - datetime.date.today()

# print(datetime.date(2020, 1, 1).weekday()) # 수요일은 2
# #print(isoweekday())