vi=input()
amia=input()
alimentacao=input()
if vi=='vertebrado' and amia=='ave' and alimentacao=='carnivoro':
  print('aguia')
elif vi=='vertebrado' and amia=='ave' and alimentacao=='onivoro':
  print('pomba')
elif vi=='vertebrado' and amia=='mamifero' and alimentacao=='onivoro':
  print('homem')
elif vi=='vertebrado' and amia=='mamifero' and alimentacao=='herbivoro':
  print('vaca')
elif vi=='invertebrado' and amia=='inseto' and alimentacao=='hematofago':
  print('pulga')
elif vi=='invertebrado' and amia=='inseto' and alimentacao=='herbivoro':
  print('lagarta')
elif vi=='invertebrado' and amia=='anelideo' and alimentacao=='hematofago':
  print('sanguessuga')
elif vi=='invertebrado' and amia=='anelideo' and alimentacao=='onivoro':
  print('minhoca')
else:
  print('Invalido')