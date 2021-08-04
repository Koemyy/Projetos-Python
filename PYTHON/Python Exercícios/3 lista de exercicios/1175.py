x=[]
y=[]
c=0
z=0

while(c<20):
    n = int(input())
    x.append(n)
    c+=1   
c=19

while(c>=0):
    y.append(x[c])
    print(f"N[{z}] = {y[z]}")
    z+=1
    c-=1
    