tempo = input().split()
i = int(tempo[0])
f = int(tempo[1])

if(i==f): 
    tempo = 24
elif(f>i): 
    tempo = f-i
else: 
    tempo = (24-i)+f

print(f"O JOGO DUROU {tempo} HORA(S)")