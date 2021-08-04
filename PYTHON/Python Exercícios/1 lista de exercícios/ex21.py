valor = float(input())
valor = int(valor*100)

print("NOTAS:")

x = int(valor//10000)

print(f"{x} nota(s) de R$ 100.00")

valor-=x*10000

x = int(valor//5000)

print(f"{x} nota(s) de R$ 50.00")

valor-=x*5000

x = int(valor//2000)

print(f"{x} nota(s) de R$ 20.00")

valor-=x*2000

x = int(valor//1000)

print(f"{x} nota(s) de R$ 10.00")

valor-=x*1000

x = int(valor//500)

print(f"{x} nota(s) de R$ 5.00")

valor-=x*500

x = int(valor//200)

print(f"{x} nota(s) de R$ 2.00")

valor-=x*200

#-------------------------------------------------------------------------------------------------------#

print("MOEDAS:")

x = int(valor//100)

print(f"{x} moeda(s) de R$ 1.00")

valor-=x*100

x = int(valor//50)

print(f"{x} moeda(s) de R$ 0.50")

valor-=x*50

x = int(valor//25)

print(f"{x} moeda(s) de R$ 0.25")

valor-=x*25

x = int(valor//10)

print(f"{x} moeda(s) de R$ 0.10")

valor-=x*10

x = int(valor//5)

print(f"{x} moeda(s) de R$ 0.05")

valor-=x*5

x = int(valor//1)

print(f"{x} moeda(s) de R$ 0.01")

valor-=x*1