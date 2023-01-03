# 다음의 딕셔너리가 주어졌을 때 한국의 면적과 가장 비슷한 국가와 그 차이를 출력하세요.

nationWidth = {
     'korea': 220877,
     'Rusia': 17098242,
     'China': 9596961,
     'France': 543965,
     'Japan': 377915,
     'England' : 242900 
    }

korea_width = nationWidth['korea']
gap = max(nationWidth.values())
closest_nation = ""

for nation, width in nationWidth.items():
    if nation == "korea":
        continue
    if int(abs(korea_width - width)) < gap:
        gap = int(abs(korea_width - width))
        closest_nation = nation

print(closest_nation, gap)