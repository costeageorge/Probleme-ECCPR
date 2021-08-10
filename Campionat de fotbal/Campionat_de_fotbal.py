nr_echipe = int(input())
nr_partide= int(input())
dictionar = {}
for i in range(nr_partide):
	lista = input().split(" ")
	if lista[0] in dictionar and lista[4] in dictionar:
		dictionar[lista[0]][1] += int(lista[1])	
		dictionar[lista[0]][2] += int(lista[3])	
		dictionar[lista[4]][1] += int(lista[3])		
		dictionar[lista[4]][2] += int(lista[1])	
		if lista[1] > lista[3]:
			dictionar[lista[0]][0] += 3
		else: 
			if lista[1] == lista[3]:
				dictionar[lista[0]][0] += 1
				dictionar[lista[4]][0] += 1	
			else:
				dictionar[lista[4]][0] += 3
	else:
		if lista[0] in dictionar:
			dictionar[lista[0]][1] += int(lista[1])		
			dictionar[lista[0]][2] += int(lista[3])	
			if lista[1] > lista[3]:
				dictionar[lista[0]][0] += 3
				dictionar[lista[4]] = [0,int(lista[3]), int(lista[1])]
			else: 
				if lista[1] == lista[3]:
					dictionar[lista[0]][0] += 1
					dictionar[lista[4]] = [1,int(lista[3]), int(lista[1])]
				else:
					dictionar[lista[4]] = [3,int(lista[3]), int(lista[1])]
			
		else:
			if lista[4] in dictionar:
				dictionar[lista[4]][1] += int(lista[3])		
				dictionar[lista[4]][2] += int(lista[1])	
				if lista[1] > lista[3]:
					dictionar[lista[0]] = [3,int(lista[1]), int(lista[3])]
				else: 
					if lista[1] == lista[3]:
						dictionar[lista[4]][0] += 1
						dictionar[lista[0]] = [1,int(lista[1]), int(lista[3])]
					else:	
						dictionar[lista[4]][0] += 3
						dictionar[lista[0]] = [0,int(lista[1]), int(lista[3])]
			else:
				if lista[1] > lista[3]:
					dictionar[lista[0]] = [3,int(lista[1]), int(lista[3])]
					dictionar[lista[4]] = [0,int(lista[3]), int(lista[1])]
				else: 
					if lista[1] == lista[3]:
						dictionar[lista[0]] = [1,int(lista[1]), int(lista[3])]
						dictionar[lista[4]] = [1,int(lista[3]), int(lista[1])]
					else:
						dictionar[lista[0]] = [0,int(lista[1]), int(lista[3])]
						dictionar[lista[4]] = [3,int(lista[3]), int(lista[1])]
dictionar = dict(sorted(dictionar.items(), key = lambda x: x[1],reverse = True))
for i in dictionar:
	print(i,end = ' ')
	for j in list(dictionar[i]):
		print(j,end = ' ')
	print('')



