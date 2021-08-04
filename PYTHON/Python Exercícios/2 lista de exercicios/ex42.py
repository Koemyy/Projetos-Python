x = 0
y = 0
h = 0

while(x < 6):
    c = float(input())
    if(c>0):
        y+=1
        h+=c    
    x+=1

x=h/y

print(f"{y} valores positivos")
print("%.1f"%x)



