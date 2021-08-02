#Timp necesar pentru rezolvare: 25-30 minute


def citire_date():                  #Functia de citire a datelor de la tastatura
    n = int(input())
    sir = input()
    return n,sir

def adaugare_lista(sir):            #Functia care imi creaza o lista cu elemente de cate 2 biti
    lista = []
    j = 0
    for i in range(2,len(sir)+1,2):
        lista.append(sir[j:i])
        j+=2
    return lista

n,sir = citire_date()
lista = adaugare_lista(sir)
dictionar = dict()
for i in lista:
    if i not in dictionar :
        dictionar[i] = lista.count(i)
r1 = max(dictionar.values())/min(dictionar.values())
r2 = sir.count('1')/sir.count('0')
print(r1,r2)
if r1 > 1.1 or r2 > 1.1:
    print (0)
else:
    print(1)
    
