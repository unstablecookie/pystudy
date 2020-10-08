#realpython.com
def merge(left,right):
	if len(left) == 0:
		return right

	if len(right) == 0:
		return left
	result = []
	left_index = right_index = 0

	while len(result) < len(left) + len(right):
		if left[left_index] <= right[right_index]:
			result.append(left[left_index])
			left_index += 1
		else:
			result.append(right[right_index])
			right_index += 1

		if right_index == len(right):
			result += left[left_index:]
			break

		if left_index == len(left):
			result += right[right_index:]
			break
	return result
def insertion_sort(array, left = 0,right = None):
	if right is None:
		right = len(array) - 1

	for f in range(left + 1, right + 1):
		key = array[f]
		item = f - 1
		while item >= left and array[item] > key:
			array[item + 1] = array[item]
			item -= 1
		array[item + 1] = key
	return array


def timsort(array):
	min_run = 3
	n = len(array)

	for f in range(0,n,min_run):
		insertion_sort(array,f,min((f + min_run - 1),n - 1))

	size = min_run
	while size < n:
		for start in range(0,n,size * 2):
			midpoint = start + size - 1
			end = min((start + size * 2 - 1),(n-1))
			merged_array = merge(
				left = array[start:midpoint + 1],
				right = array[midpoint + 1:end + 1])
			array[start:start + len(merged_array)] = merged_array
		size *= 2
	return array