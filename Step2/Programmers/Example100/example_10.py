# 올바른 괄호 문자열인지 판별하는 함수
def is_valid(s):
    stack = []  # 여는 괄호를 저장할 스택
    pair = {')': '(', ']': '[', '}': '{'}  # 닫는 괄호와 그에 상응하는 여는 괄호의 짝을 저장하는 딕셔너리
    
    # 문자열 s의 각 문자에 대해 반복
    for char in s:
        # 만약 현재 문자가 여는 괄호 중 하나라면 스택에 추가
        if char in pair.values():
            stack.append(char)
        # 만약 현재 문자가 닫는 괄호 중 하나라면
        elif char in pair:
            # 스택이 비어있거나 스택의 마지막 요소가 해당 닫는 괄호의 짝이 아니라면 False 반환
            if not stack or pair[char] != stack.pop():
                return False
    # 모든 검사를 마치고 스택이 비어있다면 모든 괄호가 올바르게 닫혔다는 의미이므로 True 반환
    # 그렇지 않다면 False 반환
    return len(stack) == 0

# 문자열을 왼쪽으로 한 칸 회전시키는 함수
def rotate(s):
    return s[1:] + s[:1]  # 첫 번째 문자를 제외한 나머지 문자열과 첫 번째 문자를 합친 새로운 문자열 반환

# 주어진 문자열 s를 회전시키면서 올바른 괄호 문자열인 경우를 세는 함수
def solution(s):
    count = 0  # 올바른 괄호 문자열이 되는 경우의 수를 세기 위한 카운터
    # 문자열의 길이만큼 반복
    for _ in range(len(s)):
        # 현재 문자열이 올바른 괄호 문자열이라면 카운터 증가
        if is_valid(s):
            count += 1
        # 문자열을 왼쪽으로 한 칸 회전
        s = rotate(s)
    # 올바른 괄호 문자열이 되는 회전 수 반환
    return count
