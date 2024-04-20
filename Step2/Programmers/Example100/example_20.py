participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
checks = [False]*len(participant)

answer = []

for i, pa in enumerate(participant):
    # print(pa)
    # print(not pa in completion)
    if not pa in completion:
        checks[i] = True

# print(checks)

for j, checks in enumerate(checks):
    if checks == True:
        answer.append(participant[j])
    
print(answer)


