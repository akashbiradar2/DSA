# bucket search
# TC(best,avg) = O(n+k), worst = O(n^2)
# sc = O(1)
def insersion_sort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr

def bucket_sort(x):
	
	arr1 = []
	
	slot_no = 10
	for i in range(slot_no):
		arr1.append([])
		
	for j in x:
		index = int(slot_no*j)
		arr1[index].append(j)
	
	for i in range(slot_no):
		arr1[i] = insersion_sort(arr1[i])
		
	k = 0
	for i in range(slot_no):
		for j in range(len(arr1[i])):
			x[k] = arr1[i][j]
			k += 1
	return x	
	
x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucket_sort(x))
		
