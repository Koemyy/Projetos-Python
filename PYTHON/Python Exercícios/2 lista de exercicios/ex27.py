coordenada = input().split()

x= float(coordenada[0])
y= float(coordenada[1])

if(x==0 and y==0):
    print("Origem")

if(x>0 and y>0):
    print("Q1")

if(x<0 and y>0):
    print("Q2")

if(x<0 and y<0):
    print("Q3")

if(x>0 and y<0):
    print("Q4")

if(x==0 and y!=0):
    print("Eixo Y")

if(x!=0 and y==0):
    print("Eixo X")