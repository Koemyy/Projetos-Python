x=[]
c=0
n=int(input())

while(c<10):
    x.append(n)
    print(f"N[{c}] = {x[c]}")
    n*=2
    c+=1