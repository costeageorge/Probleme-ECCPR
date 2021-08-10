def codare_nul(lista):
	lista1 = []
	string = ''
	for i in lista:
		if '1' in i:
			for j in i:
				string = string+j
			lista1.append('1'+string)
			string = ''
		else:	
			lista1.append('0')
	return lista1	

def codare_1(lista):
	lista1 = []
	string = ''
	for i in lista:
		if '0' in i:
			for j in i:
				string = string+j
			lista1.append('0'+string)
			string = ''
		else:	
			lista1.append('1')
	return lista1	

def decizie(lista,elem):
	str1 = "".join(codare_1(lista))
	str0 = "".join(codare_nul(lista))
	if len(str1) < len(str0):
		print("{:.2f}".format(nr_elem / (len(str1)+1)))		
		print('1')
		for i in str1:
			print (i)
	else:
		print("{:.2f}".format(nr_elem / (len(str0)+1)))	
		print('0')
		for i in str0:
			print (i)

	

nr_elem = int(input())
nr_grup = int(input())
lista_elem = []
lista = []
lista_grupuri = []
index = 1
for i in range(nr_elem):
	lista_elem.append(input())
for i in range(1,nr_elem//nr_grup+1):
	for j in range(nr_grup*(i-1),nr_grup * i):
		lista .append(lista_elem[j])
	lista_grupuri.append(lista)
	lista = []
if nr_elem % nr_grup != 0:
	elem = nr_elem-(nr_elem % nr_grup)
	lista_grupuri.append(lista_elem[elem: nr_elem+1])
decizie(lista_grupuri,nr_elem)
	
