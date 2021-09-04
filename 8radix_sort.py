# radix count
# TC(best) = O(n+k) , (avg,worst) O(nk)
# SC = O(n+k)

def counting_sort(arr,p):
	n = len(arr)
	res = [0]*n
	c = [0]*10
	for i in range(0,n):
		temp = arr[i]//p
		c[temp%10] += 1
	for i in range(1,10):
		c[i] = c[i] + c[i-1]
	
	i = n-1
	while i >= 0:
		temp = arr[i]//p
		res[c[temp%10]-1] = arr[i]
		c[temp%10] -=  1
		i=i-1
	for i in range(n):
		arr[i] = res[i]
	
def radix_count(arr):
	length = len(arr)
	maximum = max(arr)
	p = 1
	while maximum//p > 0:
		counting_sort(arr,p)
		p *= 10
		
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_count(arr)
print(arr)
