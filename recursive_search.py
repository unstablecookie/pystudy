def find(array, key):
	left, right = 0, len(array) - 1

	if left <= right:
		mid = (left + right) // 2

		if array[mid] == key:
			return array[mid]

		if array[mid] < key:
			return find(array[mid + 1:],key)
		elif array[mid] > key:
			return find(array[:mid],key)

	return False

list1 = [1,2,3,4,5,6,7,8]

res = find(list1,4)
print(res)