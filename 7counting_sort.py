# counting sort
# n: number of inputes, k: range of inputes
# TC(best, avg, worst) = O(n+k), SC = O(k)

def counting_sort(arr):
	n = len(arr)
	res = [0]*n
	c = [0]*n
	for i in range(n):
		c[arr[i]] += 1
	for i in range(1,n):
		c[i] = c[i] + c[i-1]
	i = n-1
	while i >= 0:
		res[c[arr[i]]-1] = arr[i]
		c[arr[i]] = c[arr[i]] - 1
		i -=1
	return res
	
arr = [0,5,4,4,3,2,1,8,4]
print(counting_sort(arr))
