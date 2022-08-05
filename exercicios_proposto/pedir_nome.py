"""
Pedir o nome do usuário e definir o tomanho com base nos caracteres
"""
nome = input('Digite seu nome: ')
num_carac = len(nome)

if num_carac <= 4:
    print(f'{nome} seu nome é curto!')
elif num_carac == 5 or num_carac == 6:
    print(f'{nome} seu nome é nomral!')
else:
    print(f'{nome} seu nome é grande!')