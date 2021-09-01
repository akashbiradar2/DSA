# ternary search
# TC = O(log(n)

def ternary_search(arr,l,r,x):
	if r >= l:
		
		mid1 = l + (r-l)//3
		mid2 = r - (r-l)//3
		
		if arr[mid1] == x:
			return mid1
		if arr[mid2] == x:
			return mid2
		
		if x < arr[mid1]:
			return ternary_search(arr, l, mid-1,x)
		elif x > arr[mid2]:
			return ternary_search(arr, mid2+1, r,x)
		else:
			return ternary_search(arr, mid1+1, mid2-1,x)
	else:
		return -1
arr = [0,1,1,2,3,5,8,13,21,34,55,65,66,69,75,78,80,100]		
x = 55
print(ternary_search(arr,0,len(arr)-1,x))
