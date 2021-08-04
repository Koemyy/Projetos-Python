x = int(input())
n = input().split()
menor = int(n[0])
c=0
posicao=c

while(c<x):
    if(menor>int(n[c])):
        menor=int(n[c])
        posicao=c
    c+=1

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")