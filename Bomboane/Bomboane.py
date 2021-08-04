nr_zile = int(input())
bani_zi = input().split(" ")
lista_bomboane = []
for _ in range(nr_zile):
	lista_bomboane.append(input().split(" "))
fericire = 0
bani = 0
ok = 0
for i in range(len(lista_bomboane)):
	bani = bani + int(bani_zi[i])
	if bani >= int(lista_bomboane[i][0]) :
		fericire += int(lista_bomboane[i][1])
		bani = bani - int(bani_zi[i])
	else:
		for j in range(0,i):
			if int(lista_bomboane[i][1]) < int(lista_bomboane[j][1]):
				ok = 1				
				break
		if ok == 0:
			fericire -= int(lista_bomboane[i][1])
	
print(fericire)
