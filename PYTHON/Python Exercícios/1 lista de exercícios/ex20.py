dias = int(input())

x = dias//365

dias-=x*365

y=dias//30

dias-=y*30

print(f"{x} ano(s)")
print(f"{y} mes(es)")
print(f"{dias} dia(s)")