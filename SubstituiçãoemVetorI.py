X = []
for i in range(10):
    valores = int(input())
    if valores <= 0:
        valores = 1
        X.insert(i,valores)
    else:
        X.insert(i,valores)

for i in range(10):
    print('X[{0}] = {1}'.format(i,X[i]))