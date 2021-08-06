nr_aruncari = int(input())
dictionar = {}
for i in range(nr_aruncari):
	zar = input()
	if zar not in dictionar:
		dictionar[zar] = 1
	else:
		dictionar[zar] +=1
maxim = max(dictionar.values())
if len(dictionar) == 0:
	minim = 0
else:
	minim = min(dictionar.values())
if maxim - minim < nr_aruncari/10:
	print(1)
else:
	print(0)
