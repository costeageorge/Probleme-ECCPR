nr_inst = int(input())
dictionar = {}
lista1 = []
for i in range(nr_inst):
	lista = input().split(" ")
	if lista[0] == 'lconst':
		dictionar[lista[1]] = lista[2]
	else:
		if lista[0] == 'add':
			dictionar[lista[1]] = int(dictionar[lista[2]]) + int(dictionar[lista[3]])
		else:
			if lista[0] == 'mul':
				dictionar[lista[1]] = int(dictionar[lista[2]]) * int(dictionar[lista[3]])
			else:
				if lista[0] == 'div':
					if dictionar[lista[3]] == '0':
						lista1.append("Exception: line " + str(i+1))		
						break
					else:
						dictionar[lista[1]] = int(dictionar[lista[2]]) / int(dictionar[lista[3]])
				else:				
					if lista[0] == 'print':
						lista1.append(int(dictionar[lista[1]]))
for i in lista1:
	print(i)
