#Timp necesar de rezolvare 2 ore

nr_num = int(input())
lista = input().split(" ")
lista.sort()
index = 0
tmp = -1
for i in range(1,len(lista)):
	if int(lista[i]) != int(lista[i-1]):
		if lista.count(lista[i]) == 1 or lista.count(lista[i]) == 3:
			index +=1
			if lista.count(lista[i]) == 3:
			    tmp = i
if index <= 1:
    if len(lista)%2 == 1:
	    if tmp == -1:
		    str = lista[0]
		    for i in range(1,len(lista),2):
			    str = lista[i] + str + lista[i+1]
	    else :
	        str = lista[tmp]
	        lista.pop(tmp)
	        for i in range(0,len(lista),2):
	            str = lista[i] + str + lista[i+1]
    else:
        str = ''
        for i in range(0,len(lista),2):
            str = lista[i] + str + lista[i+1]
    print(str)
else:
	print(0)
