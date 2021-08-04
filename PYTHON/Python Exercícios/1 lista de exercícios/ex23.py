valores = input().split()

a= float(valores[0])
b= float(valores[1])
c= float(valores[2])

x = b**2-4*a*c

if(a!=0 and x>=0):

    r1= (-b + x**(1/2))/(2*a)
    r2= (-b - x**(1/2))/(2*a)
    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)

else:
    print("Impossivel calcular")