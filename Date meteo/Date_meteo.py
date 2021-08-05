nr_zile = int(input())
lista_tmp = input().split(" ")
lista = []
lista.append(lista_tmp[0])
lista_tmp_final = []
for i in range(1,nr_zile):
	if int(lista_tmp[i]) >= 0 and  int(lista_tmp[i-1]) < 0 :
		lista.append(lista_tmp[i])
	else:
		if int(lista_tmp[i]) < 0 and  int(lista_tmp[i-1]) >= 0 :
			lista.append(lista_tmp[i])
		else:
			lista_tmp_final.append(lista)
			lista = []
			lista.append(lista_tmp[i])
if lista not in lista_tmp_final:
	lista_tmp_final.append(lista)
lista_max = lista_tmp_final[0]
for i in lista_tmp_final:
	if len(lista_max) <= len(i):
		lista_max = i
print(len(lista_max))
for i in lista_max:
	print(i,end = " ")
nr_poz = 0
nr_neg = 0
for i in lista_tmp:
	if int(i) >= 0:
		nr_poz +=1
	else:
		nr_neg +=1
print("")
print("+:{:.2f}% -:{:.2f}%".format(nr_poz*100/nr_zile,nr_neg*100/nr_zile))
