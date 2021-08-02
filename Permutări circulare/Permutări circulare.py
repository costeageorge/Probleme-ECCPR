Timp necesar pentru rezolvare: 30 de minute

def permutari(binar):
    lista = []
    for i in binar:
        lista.append(binar)
        binar = binar[len(binar)-1] + binar[0:len(binar)-1]
    return lista

n = int(input())
binar = bin(n).replace("0b","")
lista = permutari(binar)
lista2 = []
for i in lista:
    numar = 0
    index = len(i)-1
    for j in i:
        numar = numar  + int(j) * 2 ** index
        index -= 1
    lista2.append(numar)
print(max(lista2))
                   
