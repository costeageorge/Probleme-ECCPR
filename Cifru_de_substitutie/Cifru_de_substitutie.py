propozitie = list(input())
lista_inlocuire = input().split(" ")
dictionar = {}
for i in lista_inlocuire:
	tmp = i.split(",")
	dictionar[tmp[0]] = tmp[1]
for i in range(len(propozitie)):
	if propozitie[i] in dictionar:
		propozitie[i] = dictionar[propozitie[i]]
print("".join(propozitie))

