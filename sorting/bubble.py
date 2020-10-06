from array import array
def bubble(array):
	list1 = array.tolist()
	n = len(list1)
	for f in range(n):
		for k in range(n - f - 1):
			if array[k] > array[k + 1]:
				array[k],array[k + 1] = array[k + 1],array[k]
	return array