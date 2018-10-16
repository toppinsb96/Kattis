useless = int(input())
deck = list(map(int, input().split()))
b = True

while(b):
	i = 0
	b = False
	while(i < len(deck) - 1):
		curr = deck[i]
		nxt = deck[i+1]
		s = curr + nxt
		if(s % 2 == 0):
			deck.pop(i)
			deck.pop(i)
			b = True
		else:
			i += 1

print(len(deck))
