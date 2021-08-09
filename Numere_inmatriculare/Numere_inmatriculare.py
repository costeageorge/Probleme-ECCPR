#Timp necesar de rezolvare: 30 de minute

from sys import stdin
lista2 = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
def verificare_litere(str):
    index = 0
    for i in str:
        if i in lista2:
            index +=1
    if index == len(str):
        return "true"




str1 = 'AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS,CL, CJ, CT, CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH,SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN'
lista1 = str.split(",")
numar = '0'
while True:
    line = input()
    if line == '':
        break
    else:
	    lista = line.split(" ")
	    if lista[0] in str1:
		    if lista[1].isdecimal() and (len(lista[1]) == 2 or len(lista[1]) == 3) :
			    if lista[2].isalpha() and len(lista[2]) == 3 and  verificare_litere(lista[2])=="true":
				    print(line)

