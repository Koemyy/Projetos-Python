valor = input().split()

v1 = int(valor[0])
v2 = int(valor[1])

if(v1%v2==0 or v2%v1==0):
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")