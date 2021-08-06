#Timp necesar de rezolvare: 10-15 minute
nr_zaruri = int(input())
suma = 0
for i in range(nr_zaruri):
	lista = input().split(" ")
	for j in range(1,7):
		if str(j) not in lista:
			suma += int(j)
print(suma)
