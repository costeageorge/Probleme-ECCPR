#2:47

#Prima incercare > 2 ore
#A doua incercare 1:40

lista = input().split(" ")
nr_spatii = int(lista[0])
nr_dif_carti = int(lista[1])
dictionar = {}
for i in range(nr_dif_carti):
    lista = input().split(" ")
    dictionar[int(lista[1])] = int(lista[0])
lista_carti_raft = []
lista = []
ok = 0
suma = 0
for i in dictionar:
    #suma = 0
    while dictionar[i] != 0:
        if suma + i <= 200:
            lista.append(i)
            dictionar[i] -=1
            suma +=i
            for j in dictionar:
                if dictionar[j] != 0:
                    if suma + j <= nr_spatii:
                        lista.append(j)
                        dictionar[j] -=1
                        suma = suma + j
                        if suma + min(dictionar) > nr_spatii:
                            ok = 1
                            break
        else:
            ok = 1
        if ok == 1 or (dictionar[i] == 0 and dictionar[j] == 0):         
            lista_carti_raft.append(lista)
            lista = []
            ok = 0
            suma = 0


print(lista_carti_raft)
           

