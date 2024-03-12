# 스택 초기화
stack = []

# push 함수: 스택에 요소 추가
def push(element):
    stack.append(element)

# pop 함수: 스택의 최상단 요소 제거 및 반환
def pop():
    if not is_empty():
        return stack.pop()
    else:
        return "스택이 비어있습니다."

# peek 함수: 스택의 최상단 요소 반환
def peek():
    if not is_empty():
        return stack[-1]
    else:
        return "스택이 비어있습니다."

# is_empty 함수: 스택이 비어있는지 확인
def is_empty():
    return len(stack) == 0

# 스택 사용 예제
push(1)     # 스택에 1 추가
push(2)     # 스택에 2 추가
push(3)     # 스택에 3 추가
print(stack)  # 스택 출력: [1, 2, 3]
print(pop())  # 3 출력 및 스택에서 제거
print(peek())  # 2 출력 (스택 최상단 조회)
print(stack)  # 최종 스택 상태 출력: [1, 2]
