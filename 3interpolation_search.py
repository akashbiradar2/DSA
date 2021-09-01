# interpolation search 
# here we use a formula which gives pos
# T.C. = O(log(log(n)) , best case = O(1)

def interpolation_search(arr,l,r,x):
    if l<=r and x >= arr[l] and x <= arr[r]:
        pos = l + ((r-l)//(arr[r]-arr[l])*(x-arr[l]))
        if arr[pos] == x:
            return pos
        elif arr[pos] > x:
            return interpolation_search(arr, l, pos-1, x)
        else:
            return interpolation_search(arr, pos+1, r, x)
    else:
        return -1

arr = [0,1,1,2,3,5,8,13,21,34,55,65,66,69,75,78,80,100]
x = 55
print(interpolation_search(arr,0,len(arr)-1,x))
