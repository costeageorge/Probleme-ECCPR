def verificare_integralisti(lista_nume,lista_note):
    lista_index = []
    for i in range(len(lista_note)):
        for j in lista_note[i]:
            if int(j) < 5:
                lista_index.append(i)
                break
    for i in lista_index:
        lista_nume.pop(i)
        lista_note.pop(i)
    return lista_nume,lista_note

lista = input().split(" ")
nr_studenti = int(lista[0])
nr_discipline = int(lista[1])
nr_burse_disponibile = int(lista[2])
lista_nume = []
lista_note = []
for i in range(nr_studenti):
    lista_nume.append(input())
    lista_note.append(input().split(" "))
lista_nume,lista_note = verificare_integralisti(lista_nume,lista_note)

lista_medii = []
for i in lista_note:
    suma = 0
    for j in i:
        suma = suma +int(j)
    lista_medii.append(suma / nr_discipline)
index = 0
for i in lista_medii:
    if i > 8:
        index +=1
if index >= nr_burse_disponibile:
    index = nr_burse_disponibile
    print(index)
else:
    print(index-1)
print("{} {:.2f}".format(lista_nume[lista_medii.index(max(lista_medii))],max(lista_medii)))
