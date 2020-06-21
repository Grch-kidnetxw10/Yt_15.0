A = 0
B = 0
c = 0
lisa = []

while c <= 9:
    A = A * B
    if A * B == 0 or A * B == 1:
        A += 1
        B += 1
    lisa.append(A)
    c += 1

print(lisa[:])

x = 0
y = 0
p = []
l = 0
for x in range(1, 10):
    l = y + x
    y = y + x
    p.append(l)
print(p[:])

X = 0
Y = 0
P = []
L = 0

for X in range(-10, 10):
    L = Y + X
    P.append(L)
print(P[:])

numbE = []
numbF = []
v = 1
n = 1

for n in range(-3, 3):
    v = n * v
    numbE.append(v)
    if v == 0:
        v += 1
    if n == 5:
        break

print(numbE[:])

for n in range(-3, 3):
    if n == 0:
        n = 0.1
    if n and v == int:
        v += 0.1
        n += 0.01
    n += 0.1
    v = n / v
    n * v
    numbF.append(v)

print(numbF[:])

#def M_int(h):