mn = input().split()
m = int(mn[0])
n = int(mn[1])
c=0

while(m>0 and n>0):
    if(m>n):
        maior=m
        menor=n
    else:
        maior=n
        maior=m

    soma = 0
    while(menor<=maior):
        print(menor,end=' ')
        soma += menor
        menor += 1 

    print(f"Sum={soma}")

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])