from random import choice
from random import randint

def mutate(text, collisionsList, alphabet):
	randLit = choice(alphabet)

	fullRange = set(range(0, len(text)))
	fullRange -= set(collisionsList)
	mutateIndex = choice(list(fullRange))
	newText = text[:mutateIndex] + randLit + text[mutateIndex+1:]
	return newText

def collisionsAmount(a, b):
	amount = 0
	collisionsList = set()
	for i in range(len(a)):
		if (a[i:i+1] == b[i:i+1]):
			amount += 1
			collisionsList.add(i)
	return amount, collisionsList

# берем данные
# добавляем мутации
# вычисляем коллизию с целевыми данным
# если коллизии не равны длине строки - повторяем
def main():
	s = "кривая пеано - общее название для параметрических кривых, образ которых содержит квадрат (или, в более общем смысле, открытые области пространства)."
	alphabet = "йцукенгшщзхъфывапролджэячсмитьбю.,()- "
	data = "".join([choice(alphabet) for i in range(len(s))])
	collisionsList = set()
	curCollision = collisionsAmount(s, data)
	c = 0
	while (curCollision[0] != len(s)):
		print(c,"::",data)
		data = mutate(data, collisionsList, alphabet)
		curCollision = collisionsAmount(s, data)
		collisionsList = curCollision[1]
		c += 1
	print(c,"::",data)
	
if __name__ == "__main__":
	main()
