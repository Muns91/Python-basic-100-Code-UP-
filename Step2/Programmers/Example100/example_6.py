# 2024년 4월 5일
# 실패율

# 실패율의 정의 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# 전체 스테이지 개수가 N, 게임을 이용하는 사용자가 현재 멈춰 있는 스테이지의 번호가 담긴 배열 stages가 주어질 때 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 반환하라


n = 5 # 스테이지의 수
stages = [2,1,6,2,4,3,3] # 게임을 이용하는 사용자가 멈춰 있는 스테이지 번호

challenger = [0]*(n+2)
for stage in stages:
    challenger[stage]+=1

print(challenger)

fails = {}
total = len(stages)

for i in range(1, n+1):
    if challenger[i] ==0:
        fails[i] = 0
    else:
        fails[i] = challenger[i]/total
        total -=challenger[i]
print(fails)

result = sorted(fails, key=lambda x : fails[x], reverse=True)

print(result)

