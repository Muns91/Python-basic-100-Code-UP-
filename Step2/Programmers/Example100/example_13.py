def solution(board, moves):
    answer = 0
    
    r=len(board)
    c=len(board[0])
    
    basket = []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] !=0:
                basket.append(board[i][m-1])
                board[i][m-1]=0
                
                if len(basket) >=2 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer +=2
                break
    
    
    
    return answer