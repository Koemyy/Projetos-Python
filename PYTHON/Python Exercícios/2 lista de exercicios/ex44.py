c=0
w=0

while(c<5):
    x=int(input())

    if(x%2==0):     
        w+=1
    c+=1

print(f"{w} valores pares")