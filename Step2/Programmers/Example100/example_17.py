# 2024년 4월 17일
# 카드 뭉치

from collections import deque

cards1=["i", "drink", "water"]
		
cards2 = ["want", "to"]	

goal = ["i", "want", "to", "drink", "water"]	

def solution(cards1, cards2, goal):
    for g in goal:
        
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

print(solution(cards1, cards2, goal))

