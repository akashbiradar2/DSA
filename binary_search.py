# binary search
# time complaxity of binary search is O(logn) and best case is O(1)

def binary_search(arr,l,r,x):
    if r>=l:
        mid = l + (r-1)//2
        
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            
            return binary_search(arr,l,mid-1,x)
        
        else:
            return binary_search(arr,mid+1,r,x)
    else:
        return -1

arr = [0,1,1,2,3,5,8,13,21,34,55,65,66,69,75,78,80,100]
x = 8
print(binary_search(arr,0,len(arr)-1,x))
        
        
