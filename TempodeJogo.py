x = input().split()
i = int(x[0])
f = int(x[1])
if i < f: 
    t = f - i
else:
    t = (24 - i) + f
print("O JOGO DUROU %i HORA(S)"%t)