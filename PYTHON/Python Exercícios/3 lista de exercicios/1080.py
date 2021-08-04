c=1
x=int(input())
maior=x
posicao=c

while(c<100):
    x=int(input())
    c+=1

    if(x>maior):
        maior=x
        posicao=c

print(f"{maior}")
print(f"{posicao}")