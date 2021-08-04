x=int(input())
c=0
z=0
w=0

while(c<x):
    y=int(input())
    if(y>=10 and y<=20):
        z+=1
    else:
        w+=1
    c+=1

print(f"{z} in")
print(f"{w} out")
