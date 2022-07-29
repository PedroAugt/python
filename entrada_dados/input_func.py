# função input

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
ano_nascimento = 2022 - int(idade)

print()
print(f'O usuário de nome {nome} tem o total de {idade} anos!!\n'
      f'Olá {nome}, bem vindo!!\n'
      f'Você nasceu em {ano_nascimento}')
