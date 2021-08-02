#Timp necesar pentru rezolvare: 20-25 de minute

n = int(input())
nr_cmp_max = 0
nr_loturi_bune = 0
for i in range(n):
    nr_cmp = int(input())
    if nr_cmp_max < nr_cmp:
        nr_cmp_max = nr_cmp
    lista_cmp = input().split(" ")
    nr_R = lista_cmp.count("R")
    nr_T = lista_cmp.count("T")
    nr_C = lista_cmp.count("C")
    if nr_C > 0 and nr_R > 0 and nr_T > 0:
        if nr_C >= nr_T  and nr_R >= nr_C:
            nr_loturi_bune +=1
        
print(nr_loturi_bune,nr_cmp_max)
