#Timp necesar pentru rezolvare 10-15 minute


n = int(input())
dictionar = {}
ok = 0
carte_adaugata = "JOC OK"
for i in range(n):
    carte = input()
    if carte in dictionar:
        dictionar[carte] +=1
    else:
        dictionar[carte]=1
    if dictionar[carte] == 3 and ok == 0:
        carte_adaugata = carte
        ok = 1
print(carte_adaugata)
