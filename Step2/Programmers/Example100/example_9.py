

decimal = 10

def solution(decimal):

    stack = []

    while decimal>0:

        reminder = decimal%2
        stack.append(str(reminder))
        decimal //=2
    
    binary = ""

    while stack:
        binary += stack.pop()
    
    return binary

print(solution(decimal))


