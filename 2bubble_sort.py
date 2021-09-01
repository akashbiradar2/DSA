# bubble sort
# tc (avg,best,worst) = O(n^2)
# sc = O(1)

def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [7,34,6,12,76,89,15,2,5,11,54,84,95,50,47,5]
bubble_sort(arr)
print(arr)
		
