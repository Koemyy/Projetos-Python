x=int(input())
c=0

while(c<x):
    y = int(input())

    if(y == 0):
        print("NULL")
    elif(y%2==0 and y>=0):
        print("EVEN POSITIVE")
    elif(y%2==0 and y<=0):
        print("EVEN NEGATIVE")
    elif(y%2!=0 and y>=0):
        print("ODD POSITIVE")
    elif(y%2!=0 and y<=0):
        print("ODD NEGATIVE")
    c+=1