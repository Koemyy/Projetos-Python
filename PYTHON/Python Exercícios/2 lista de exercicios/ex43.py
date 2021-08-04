c=0
y=0
h=0
z=0
w=0

while(c<5):
    x=int(input())

    if(x%2==0):     
        w+=1
    if(x%2!=0):           
        z+=1
    if(x>0):
        y+=1
    if(x<0):
        h+=1
    c+=1

print(f"{w} valor(es) par(es)")
print(f"{z} valor(es) impar(es)") 
print(f"{y} valor(es) positivo(s)") 
print(f"{h} valor(es) negativo(s)")  