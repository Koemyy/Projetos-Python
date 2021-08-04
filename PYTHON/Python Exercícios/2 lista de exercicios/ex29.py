valor = input().split()

v1 = float(valor[0])
v2 = float(valor[1])
v3 = float(valor[2])

if(v2>v1 and v2>v3):
    aux = v1
    v1 = v2
    v2 = aux
elif(v3>v1 and v3>v2):
    aux = v1
    v1 = v3
    v3 = aux

if(v1<v2+v3):
    x = v1 + v2 + v3 
    print("Perimetro = %.1f"%x)

else:
    x = (v1+v2)*v3/2
    print("Area = %.1f"%x)