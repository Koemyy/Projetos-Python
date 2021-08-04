valor = input().split()
v1 = int(valor[0])
v2 = int(valor[1])

while(v1!=0 and v2!=0):
    if(v1>0 and v2>0):
        print("primeiro")
    if(v1>0 and v2<0):
        print("quarto")
    if(v1<0 and v2<0):
        print("terceiro")
    if(v1<0 and v2>0):
        print("segundo")

    valor = input().split()
    v1 = int(valor[0])
    v2 = int(valor[1])