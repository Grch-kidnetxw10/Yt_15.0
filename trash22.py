numbE = []
numbF = []
v = 1
n = 1


def Mnum_(a):
    for v in range(0, 5):
        if a[0] > a[1] and a[0] > a[2] and a[0] > a[3] and a[0] > a[4] and a[0] > a[5]:
            print(a[v], "es el numero mayor de la lista")
            return True
        elif a[1] > a[0] and a[1] > a[2] and a[1] > a[3] and a[1] > a[4] and a[1] > a[5]:
            print(a[v], "es el numero mayor de la lista")
            return True
        elif a[2] > a[0] and a[2] > a[1] and a[2] > a[3] and a[2] > a[4] and a[2] > a[5]:
            print(a[v], "es el numero mayor de la lista")
            return True
        elif a[3] > a[0] and a[3] > a[1] and a[3] > a[2] and a[3] > a[4] and a[3] > a[5]:
            print(a[v], "es el numero mayor de la lista")
            return True
        elif a[4] > a[0] and a[4] > a[1] and a[4] > a[2] and a[4] > a[3] and a[4] > a[5]:
            print(a[v], "es el numero mayor de la lista")
            return True
        else:
            print(a[5], "es el numero mayor de la lista")
            return True


for n in range(1, 7):
    v = n * v
    numbE.append(v)
    if v == 1 and v == 1:
        v += 1

print(numbE[:])


for n in range(1, 7):
    if n and v == int:
        v += 0.1
        n += 0.01
    v = n / v
    n * v
    numbF.append(v)

print(numbF[:])

Mnum_(numbE)
Mnum_(numbF)
