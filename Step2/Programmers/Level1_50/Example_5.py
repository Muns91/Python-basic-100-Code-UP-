import datetime

def solution(a, b):
    
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    print(datetime.datetime(2016, a, b).weekday())
    answer = t[datetime.datetime(2016, a, b).weekday()]
    
    return answer

print(solution(5, 24))