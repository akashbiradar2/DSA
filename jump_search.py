# jump search
# time comp. = underroot(n), best case= (1)
import math
def jump_search(arr,x):
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step,n)-1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < x:
        prev += 1
        if prev == min(step,n):
            return -1
    
    if arr[prev] == x:
        return prev
    
    return -1


arr = [0,1,1,2,3,5,8,13,21,34,55,65,66,69,75,78,80,100]
x = 55
print(jump_search(arr,x))
print(arr[10])
