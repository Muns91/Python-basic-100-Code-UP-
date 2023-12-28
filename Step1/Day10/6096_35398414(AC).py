location = []

for i in range(19):
    location.append([])

    for j in range(19):
        location[i].append(0)

for i in range(19):
    location[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        if location[x-1][j] == 0:
            location[x-1][j] = 1
        else:
            location[x-1][j] = 0
        if location[j][y-1] == 0:
            location[j][y-1] = 1
        else:
            location[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(location[i][j], end=" ")
    print()
