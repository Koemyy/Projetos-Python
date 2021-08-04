media = input().split()

n1= float(media[0])
n2= float(media[1])
n3= float(media[2])
n4= float(media[3])

x=(n1*2+n2*3+n3*4+n4*1)/10
print("Media: %.1f"%x)

if(x>=7):
    print("Aluno aprovado.")

elif(x<5):
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")
    notaexame= float (input())
    print("Nota do exame: %.1f"%notaexame)
    
    z=(x+notaexame)/2
    
    if(z>=5):
        print("Aluno aprovado.")
     
    elif(z<5):
        print("Aluno reprovado.")
    
    print("Media final: %.1f"%z)