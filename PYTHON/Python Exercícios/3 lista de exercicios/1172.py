x = []
contador = 0
while(contador<10):
    n = int(input())
    if(n<=0):
        n=1
    x.append(n)
    contador+=1

contador = 0
while(contador<10):
    print(f"X[{contador}] = {x[contador]}")
    contador += 1