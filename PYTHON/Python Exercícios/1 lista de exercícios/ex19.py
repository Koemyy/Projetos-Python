segundos = int(input())

x = segundos//3600

segundos-=x*3600

y=segundos//60

segundos-=y*60

print(f"{x}:{y}:{segundos}")