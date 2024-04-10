# 2024년 4월 10일
# 짝지어 제거하기

s="baabaa"
x = len(s)
stack = []

for c in s:
    if stack and stack[-1] ==c:
        stack.pop()
    else:
        stack.append(c)
    
print(int(not stack))


