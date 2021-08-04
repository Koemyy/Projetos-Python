abc = input().split()
pi = float(3.14159)

a= float(abc[0])
b= float(abc[1])
c= float(abc[2])

x = a*c/2
z =  pi*(c**2)
y = (a+b)*c/2
w = b**2
q = a*b

print("TRIANGULO:  %.3f"%x)
print("CIRCULO:  %.3f"%z)
print("TRAPEZIO:  %.3f"%y)
print("QUADRADO:  %.3f"%w)
print("RETANGULO:  %.3f"%q)
