crescente = input().split()

v1 = int(crescente[0])
v2 = int(crescente[1])
v3 = int(crescente[2])

if(v1 < v2 and v1 < v3):
    print(f"{v1}")
    if(v2 < v3):
        print(f"{v2}")
        print(f"{v3}")
    else:
        print(f"{v3}")
        print(f"{v2}")

if(v2 < v1 and v2 < v3):
    print(f"{v2}")
    if(v1 < v3):
        print(f"{v1}")
        print(f"{v3}")
    else:
        print(f"{v3}")
        print(f"{v1}")

if(v3 < v1 and v3 < v2):
    print(f"{v3}")
    if(v2 < v1):
        print(f"{v2}")
        print(f"{v1}")
    else:
        print(f"{v1}")
        print(f"{v2}")

print(f"\n{v1}")
print(f"{v2}")
print(f"{v3}")
