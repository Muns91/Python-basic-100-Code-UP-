arr = [1 ,2, 3, 4, 8]
target = 6



def count_sort(arr, k):
    hash_taple = [0] *(k+1)
    
    for num in arr:
        if num <= k:
            hash_taple[num] = 1
    
    return hash_taple
    
def solution(arr, target):
    hash_taple = count_sort(arr, target)

    for num in arr:
        complement = target-num

        if (complement != num and complement>=0 & complement<=target and hash_taple[complement]==1):
            return True
        
    return False

print(solution(arr, target))
