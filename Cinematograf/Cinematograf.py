#Timp necesar pentru rezolvare: 35-40 de minute

ora = input().split(":")
n = int(input())
ora_film=[]
pret = []
nume = []
lista_index = []
for i in range(n):
    lista = input().split(" ")
    ora_film.append(lista[0].split(":"))
    pret.append(lista[1])
    nume.append(lista[2])
diferenta_ore = []
for j in ora_film:
    if int(j[0])-int(ora[0]) <= 0 and int(j[1])-int(ora[1]) >= 0 :
        diferenta_ore.append([-int(j[0])+int(ora[0]),int(j[1])-int(ora[1])])
    if int(j[0])-int(ora[0]) >= 0 and int(j[1])-int(ora[1]) <= 0 :
        diferenta_ore.append([int(j[0])-int(ora[0]),-int(j[1])+int(ora[1])])
    if int(j[0])-int(ora[0]) < 0 and int(j[1])-int(ora[1]) < 0 :
        diferenta_ore.append([-int(j[0])+int(ora[0]),-int(j[1])+int(ora[1])])
    if int(j[0])-int(ora[0]) > 0 and int(j[1])-int(ora[1]) > 0 :
        diferenta_ore.append([int(j[0])-int(ora[0]),int(j[1])-int(ora[1])])
for i in range(len(diferenta_ore)):
    if min(diferenta_ore) == diferenta_ore[i]:
        lista_index.append(i)
pret_min = int(max(pret))
for i in lista_index:
    if pret_min > int(pret[i]):
        pret_min = int(pret[i])
        index = i
print(nume[index])
