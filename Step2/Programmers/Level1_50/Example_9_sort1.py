# 정렬 문제 1

array=[1, 5, 2, 6, 3, 7, 4]	
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
answer = []

for i, j, k in commands:
    
    set = []
    for a in range(i-1, j):
        set.append(array[a])

    set.sort()   
    answer.append(set[k-1])


print(answer)