# 2024년 4월 6일
# 괄호 짝 맞추기




s = '(())()'

def solution(s):
    stack = []

    for i in s:
        
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
    
print(solution(s))
            
    

    
    
