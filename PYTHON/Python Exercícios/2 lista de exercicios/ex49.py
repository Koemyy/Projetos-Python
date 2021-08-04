x = int(input())
y = int(input())
z = 0

if(y>=x):
    maior = y
    y = x
    x = maior
y+=1
while(x>y):
    if(y%2!=0):
        z+=y
    y+=1

print(f"{z}")