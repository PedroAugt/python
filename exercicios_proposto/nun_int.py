"""
Um programa que recebe um número inteiro, o programa retorna se ele é par ou impar
caso o usuário não digite um número, ele retorna erro.
"""

# num1 = input('Digite um número: ')
# try:
#     num1 = int(num1)
#     resto = num1 %2
#
#     if (resto == 0):
#         print(f'O {num1} é um número par!')
#     else:
#         print(f'O {num1} é um número impar!')
# except:
#     print('Erro!')
#
# ou poderia ter feito assim

num1 = input('Digite um número: ')

if num1.isdigit():
    num1 = int(num1)
    resto = num1 % 2
    if (resto == 0):
        print(f'O {num1} é um número par!')
    else:
        print(f'O {num1} é um número impar!')
else:
    print('Erro!')
