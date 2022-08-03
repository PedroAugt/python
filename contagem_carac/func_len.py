"""
len não funciona com tipos int, len retorna os valores em int
"""

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Erro, você precisa digitar pelo menos 6 caracteres')
else:
    print('Você passou!')