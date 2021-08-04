print("Escolha seu lanche")

x = input().split()

codigo= float(x[0])
quantidade= float(x[1])


if(codigo==1):
    z=4*quantidade

if(codigo==2):
    z=4.50*quantidade

if(codigo==3):
    z=5*quantidade

if(codigo==4):
    z=2*quantidade

if(codigo==5):
    z=1.50*quantidade

print("Total: R$ %.2f"%z)