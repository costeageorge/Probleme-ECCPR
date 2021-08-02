#Timp necesar pentru rezolvare: 30-35 de minute

sir="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numere=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
dictionar ={}
for i in range(len(sir)):
    dictionar[numere[i]] = sir[i]
mesaj = input()
lista = []
index = 0
while index < len(mesaj):
    if mesaj[index]+mesaj[index+1] != '00':
        if int(mesaj[index]+mesaj[index+1]) < 27:
            numar = int(mesaj[index]+mesaj[index+1])
            if numar in dictionar :
                lista.append(dictionar[numar])
                index +=2
        else:
            numar = int(mesaj[index])
            lista.append(dictionar[numar])
            index +=1
    else:
        lista.append(" ")
        index +=2
for i in lista:
    print(i,end='')
