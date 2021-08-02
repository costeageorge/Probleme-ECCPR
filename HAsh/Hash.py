#Timp necesar pentru rezolvare: ~60 minute



def citire_numere():                        #Functia citeste datele de la tastatura si returneaza N,k si lista de numere
    sir = input()
    lista = sir.split(" ")
    N = int(lista[0])
    k = int(lista[1])
    sir = input()
    lista_numere = sir.split(" ")
    return N,k,lista_numere

def diferenta_numere(cifra1,cifra2):        #Functia face diferenta celor doua cifre consecutive si o returneaza, vefificand care cifra este mai mare
    if cifra1-cifra2 > 0:
        return str(cifra1-cifra2)
    else:
        return str(cifra2-cifra1)



def cod_hash(numar,k):                      #Functia realizeaza codarea hash pentru fiecare numar din lista citita
    lista2 = []
    for i in range(k):
        lista = []    
        if int(numar) > 10:
            for j in range(len(numar)-1):
                lista.append(diferenta_numere(int(numar[j]),int(numar[j+1])))
            lista2.append( "".join(lista))
            numar = lista2[i-1]
        else:
            lista2.append(numar)
    return lista2



def maximul(lista):                         #Functia returneaza maximul din lista numerelor codate
    lista_rezultate = []
    for i in range(len(lista)):
        suma = 0
        for j in lista[i]:
            suma = suma + int(j)
        lista_rezultate.append(suma)
    return max(lista_rezultate)




N,k,lista_numere = citire_numere()
lista = []
for temp in lista_numere:
    lista.append(cod_hash(temp,k))       
print(maximul(lista))
