#realpython.com
from array import array

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

def merge_sort(array):
	list1 = array.tolist()
	if len(list1) < 2:
		return list1

	midpoint = len(list1) // 2
	return merge(
		left = merge_sort(array[:midpoint]),
		right = merge_sort(array[midpoint:]))