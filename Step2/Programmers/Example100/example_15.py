from collections import deque

N = int(input())
K = int(input())

queue =deque(range(1, N+1))
# print(queue)
while len(queue)>1:
    
    for _ in range(K-1):
        queue.append(queue.popleft())
        # print(queue)
        queue.popleft()
        # print(queue)
    print()

print(queue[0])

