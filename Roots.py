import math
x=int(input('Digite um numero:'))
r=math.sqrt(x)
print(f'a raiz de {x} é arredundada para {math.ceil(r)}')
print(f'a raiz de {x} é arredundada tabem para {math.floor(r)}')