'''
입력
["12:30", "13:20", "14:13"]
"12:40"

출력
['지나갔습니다', '0시간 40분', '1시간 33분']
'''

def solution(bus, time):
    res = []

    for i in bus:
        b_h, b_m = i.split(':')
        t_h, t_m = time.split(':')
        b_m = int(b_h) * 60 + int(b_m)
        t_m = int(t_h) * 60 + int(t_m)

        if b_m < t_m:
            res.append("지나갔습니다.")
        else:
            gap = b_m - t_m
            h = gap // 60
            m = gap % 60
            res.append(f"{h}시간 {m}분")

    print(res)

solution(["12:30", "13:20", "14:13"], "12:40")