#realpython.com

from random import randint

def quicksort(array):
	if len(array) < 2:
		return array

	low,sam,high = [],[],[]
	