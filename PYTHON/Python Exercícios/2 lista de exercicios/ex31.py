triangulo = input().split()

a = float(triangulo[0])
b = float(triangulo[1])
c = float(triangulo[2])

if(a >= b and a >= c):
    maior = a

elif(b >= a and b >= c):
    maior = b
    b = a
    a = maior

else:
    maior = c
    c = a
    a = maior

if(a >= b+c):
    print("NAO FORMA TRIANGULO")
    exit()

if(a**2==b**2+c**2):
    print("TRIANGULO RETANGULO")

if(a**2>b**2+c**2):
    print("TRIANGULO OBTUSANGULO")

if(a**2<b**2+c**2):
    print("TRIANGULO ACUTANGULO")

if(a==b==c):
    print("TRIANGULO EQUILATERO")

elif(a==b or a==c or b==c):
    print("TRIANGULO ISOSCELES")