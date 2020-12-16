from random import shuffle
from random import choice
from timeit import timeit

def quickSort(unsortedList: list):
	"""
	O(n*log2(n))
	"""
	if len(unsortedList) < 2:
		return unsortedList
	else:
		#pivot = unsortedList[len(unsortedList)//2] #middle value in pivot
		#pivot = choice(unsortedList) #random value in pivot
		pivot = unsortedList[0] #first value in pivot
		lessThen = [i for i in unsortedList[1:] if i <= pivot]
		greaterThen = [i for i in unsortedList[1:] if i > pivot]
		return quickSort(lessThen) + [pivot] + quickSort(greaterThen)


myUnsortedList = [0,3,5,7,3,45,2,34,12,9]
randomUnsortedList = list(range(0,10000000))
shuffle(randomUnsortedList)
prepareUnsortedList = randomUnsortedList
tryValue = 1
elapsedTime = timeit('quickSort(prepareUnsortedList)', 'from __main__ import prepareUnsortedList, quickSort', number=tryValue)/tryValue

print(elapsedTime)