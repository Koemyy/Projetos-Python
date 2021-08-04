peca1 = input().split()
peca2 = input().split()

quantidade1 = int(peca1[1])
preco1 = float(peca1[2])

quantidade2 = int(peca2[1])
preco2 = float(peca2[2])

total = quantidade1 * preco1 + quantidade2*preco2

print("VALOR A PAGAR: R$ %.2f"%total)