# find numbers only(list should be sorted beforehand)
def find(array, val):
	left,right = 0,len(array) - 1

	while left <= right:
		mid = (left + right) // 2
		if array[mid] == val:
			return mid

		if array[mid] < val:
			left = mid + 1
		elif array[mid] > val:
			right = mid - 1
	return False



#looking for a paticular string length
ff = ['topkeks','suchwow','wut','aIsForApple']
ff.sort(key=len)

def find_str(array, val):
	left,right = 0,len(array,) - 1

	while left <= right:
		mid = (left + right) // 2
		if len(array[mid]) == val:
			return array[mid]

		if len(array[mid]) < val:
			left = mid + 1
		elif len(array[mid]) > val:
			right = mid - 1
	return False

result = find_str(ff,3)
print(result)