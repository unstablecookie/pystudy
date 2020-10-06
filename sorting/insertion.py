from array import array

def insert(array):
	list1 = array.tolist()
	for f in range(1,len(list1)):
		item = list1[f]
		k = f - 1
		while k >= 0 and list1[k] > item:
			list1[k + 1] = list1[k]
			k -= 1
		list1[k + 1] = item
	return list1