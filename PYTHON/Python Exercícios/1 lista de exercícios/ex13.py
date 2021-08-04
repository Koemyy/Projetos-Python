abc = input().split()

a= int(abc[0])
b= int(abc[1])
c= int(abc[2])

maiorab = int((a+b+abs(a-b))/2)

maiorabc = int((maiorab+c+abs(maiorab-c))/2)

print(f"{maiorabc} eh o maior")

