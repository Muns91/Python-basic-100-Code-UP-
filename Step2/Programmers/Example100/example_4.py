# 2024년 4월 4일
# 모의고사
# 유형 : 완전 탐색

# 수포자는 수학을 포기한 사람을 줄인 표현입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려고 합니다.
# 수포자는 1번부터 마지막 문제까지 다음과 같이 찍습니다.


# 1번 문제부터 마지막 문제까지의 정답이 순서대로 저장된 배열 answer가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 반환하도록 함수를 만드시오.

answers = list(map(int, input().split()))

human1 = [1, 2, 3, 4, 5]
human2 = [2, 1, 2, 3, 2, 4, 2, 5]
human3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

patterns = [human1, human2, human3]

print(len(patterns))

arr = [0]*3

for i, answer in enumerate(answers):
    print("ans : ", answer)
    for j, pattern in enumerate(patterns):
        print(j, pattern)

        if answer == pattern[i%len(pattern)]:


            arr[j] += 1

max_score = max(arr)
score_set = []

for i, score in enumerate(arr):
    if score == max_score:
        score_set.append(i+1)

print(score_set)
