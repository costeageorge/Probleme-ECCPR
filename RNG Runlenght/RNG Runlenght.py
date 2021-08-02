#timp necesar de rezolvare: 40-45 de minute




n = int(input())
sir = input()
index_anterior =0
lista1 = []
dictionar = {}
for i in range(len(sir)):
    if sir[i] == '0' :
       lista1.append(sir[index_anterior:i])
       index_anterior = i
lista1.append(sir[index_anterior:len(sir)])  
for i in range(len(lista1)):
    lista1[i] = lista1[i].replace('0',"")
for i in lista1:
    if i != "":
        if i in dictionar:
            dictionar[i] += 1
        else:
            dictionar[i] = 1
temp = 1
ok = 1
x = len(dictionar)
for i in range(x):
    temp2 = temp * 10 + 1
    if str(temp) not in dictionar:
        dictionar[str(temp)] = 0
    if str(temp) in dictionar and str(temp2) in dictionar:
        if dictionar[str(temp)] < dictionar[str(temp2)]:
            ok = 0
            break
    temp = temp2
temp = 1
for i in range(len(dictionar)):
    print(dictionar[str(temp)],end=' ')
    temp = temp * 10 + 1
print("")
print(ok)    
                        
    
