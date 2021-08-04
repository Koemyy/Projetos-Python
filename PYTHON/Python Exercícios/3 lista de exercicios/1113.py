valor = input().split()
v1 = int(valor[0])
v2 = int(valor[1])

while(v1!=v2):

    if(v1>v2):
        print("Decrescente")
    else:
        print("Crescente")

    valor = input().split()
    v1 = int(valor[0])
    v2 = int(valor[1])