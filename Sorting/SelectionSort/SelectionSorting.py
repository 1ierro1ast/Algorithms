from random import shuffle
from timeit import timeit

def findSmallest(unsortedArray):
	smallest = unsortedArray[0]
	smallestIndex = 0
	for i in range(1, len(unsortedArray)):
		if(unsortedArray[i] < smallest):
			smallest = unsortedArray[i]
			smallestIndex = i
	return smallestIndex

def selectionSort(unsortedArray):
	"""
	O(n^2)
	"""
	sortedArray = []
	for i in range(len(unsortedArray)):
		smallest = findSmallest(unsortedArray)
		sortedArray.append(unsortedArray.pop(smallest))
	return sortedArray

myUnsortedArray = [0, 24, 23, 989, 1, 2, 65, 5, 8, 9, 13, 12, 64, 6, 0]

randomUnsortedArray = list(range(0,10000))
shuffle(randomUnsortedArray)
prepareUnsortedArray = randomUnsortedArray
tryValue = 100
elapsedTime = timeit('selectionSort(prepareUnsortedArray)', 'from __main__ import prepareUnsortedArray, selectionSort, findSmallest', number=tryValue)/tryValue
print(elapsedTime)
