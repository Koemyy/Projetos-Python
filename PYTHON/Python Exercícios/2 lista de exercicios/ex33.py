jogo = input().split()

hi = int(jogo[0])
mi = int(jogo[1])
hf = int(jogo[2])
mf = int(jogo[3])

x=hi*60+mi
z=hf*60+mf

if(z==x):
    jogo=24*60

elif(z>x):
    jogo=z-x

else: 
    jogo=(24*60-x)+z

horas=jogo//60
jogo-=horas*60

print(f"O JOGO DUROU {horas} HORA(S) E {jogo} MINUTO(S)")