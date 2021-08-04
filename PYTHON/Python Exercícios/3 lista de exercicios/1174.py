a=[]
c=0

while(c<100):
    n = float(input())
    a.append(n)
    c+=1

c=0

while(c<100):
    if(a[c]<=10):
        print("A[",c,"] = %.1f"%a[c],sep='')
    c+=1