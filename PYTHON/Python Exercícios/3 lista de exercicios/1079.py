x=int(input())
c=0

while(c<x):
    notas=input().split()
    n1 = float(notas[0])
    n2 = float(notas[1])
    n3 = float(notas[2])

    z=(n1*2+n2*3+n3*5)/10
    print("%.1f"%z)
    c+=1