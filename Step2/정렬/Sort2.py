n = int(input())
arr = []

for i in range(n):
    info_data = input().split()
    arr.append((info_data[0], int(info_data[1])))

arr = sorted(arr, key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')


