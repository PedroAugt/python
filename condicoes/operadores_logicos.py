"""
operadores lógicos and, or, not
"""

a = 2
b = 2
c = 3

print(a == b and b < c)
print(a == b or b < c)
print(not a == b and not b < c)

variavel_vazia = ''
nome = 'Pedro'

if not variavel_vazia:
    print('Preencha o campo vazio')
if 'e' in nome:
    print('Existe a letra E no seu nome')