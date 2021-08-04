valor = int(input())

print(f"{valor}")

x = valor//100

print(f"{x} nota(s) de R$ 100,00")

valor-=x*100

x = valor//50

print(f"{x} nota(s) de R$ 50,00")

valor-=x*50

x = valor//20

print(f"{x} nota(s) de R$ 20,00")

valor-=x*20

x = valor//10

print(f"{x} nota(s) de R$ 10,00")

valor-=x*10

x = valor//5

print(f"{x} nota(s) de R$ 5,00")

valor-=x*5

x = valor//2

print(f"{x} nota(s) de R$ 2,00")

valor-=x*2

x = valor//1

print(f"{x} nota(s) de R$ 1,00")
