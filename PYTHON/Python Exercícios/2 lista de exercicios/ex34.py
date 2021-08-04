sal = float(input())

if(sal>=0 and sal <=400.00):
    quinze=15
    x=sal*quinze/100
    z=sal+x

    print("Novo salario: %.2f"%z)
    print("Reajuste ganho: %.2f"%x)
    print(f"Em percentual: {quinze} %")

if(sal>=400.01 and sal <=800.00):
    doze=12
    x=sal*doze/100
    z=sal+x

    print("Novo salario: %.2f"%z)
    print("Reajuste ganho: %.2f"%x)
    print(f"Em percentual: {doze} %")

if(sal>=800.01 and sal <=1200.00):
    dez=10
    x=sal*dez/100
    z=sal+x

    print("Novo salario: %.2f"%z)
    print("Reajuste ganho: %.2f"%x)
    print(f"Em percentual: {dez} %")

if(sal>=1200.01 and sal <=2000.00):
    sete=7
    x=sal*sete/100
    z=sal+x

    print("Novo salario: %.2f"%z)
    print("Reajuste ganho: %.2f"%x)
    print(f"Em percentual: {sete} %")

if(sal>2000.00):
    quatro=4
    x=sal*quatro/100
    z=sal+x

    print("Novo salario: %.2f"%z)
    print("Reajuste ganho: %.2f"%x)
    print(f"Em percentual: {quatro} %")


