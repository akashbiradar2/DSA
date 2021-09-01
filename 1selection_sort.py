# selection sorted
# TC(best, avg, worst) = O(n^2)
# SC = o(1)

def selection_sort(arr):
	for i in range(len(arr)):
		small = i
		for j in range(i+1,len(arr)):
			if arr[small] > arr[j]:
				small = j
		arr[i],arr[small] = arr[small],arr[i]

arr = [7,34,6,12,76,89,15,2,5,11,54,84,95,50,47,5]
selection_sort(arr)
print(arr)
