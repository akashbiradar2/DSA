# shell sort
# it is improvement over bubble sort
# TC(best) = O(nlogn) (avg,worst) = O(nlogn^2)
# SC = o(1) 

def shellSort(arr):
	gap = len(arr) // 2 

	while gap > 0:
		i = 0
		j = gap
		while j < len(arr):
	
			if arr[i] >arr[j]:
				arr[i],arr[j] = arr[j],arr[i]
			
			i += 1
			j += 1
			k = i
			while k - gap > -1:

				if arr[k - gap] > arr[k]:
					arr[k-gap],arr[k] = arr[k],arr[k-gap]
				k -= 1

		gap //= 2

arr2 = [12, 34, 54, 2, 3]
shellSort(arr2)
print("sorted array",arr2)
