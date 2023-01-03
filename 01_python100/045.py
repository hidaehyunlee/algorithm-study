import datetime
import time

# date = datetime.datetime.today()
# print(date.year)

s = time.time() # second 단위
m = s / 60
h = m / 60
d = h / 24
y = d / 365 # 1970 부터 몇 년이 지났는지
this_year = int(y + 1970)

print(this_year)
