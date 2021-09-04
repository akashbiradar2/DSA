def quick_sort(arr):
	n = len(arr)
	if n <= 1:
		return arr
	else:
		pivot = arr.pop()
		arr_lower = []
		arr_upper = []
		
	for i in arr:
		if i < pivot:
			arr_lower.append(i)
		else:
			arr_upper.append(i)
	return quick_sort(arr_lower) + [pivot] + quick_sort(arr_upper)
	
arr = [22,34,2,3,2,89,45,23,77,90,123,45,87,98,34,65,56,23,11,17,92,28,33,63,73,1,0]
print(quick_sort(arr))
