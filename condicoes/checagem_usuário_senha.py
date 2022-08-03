usuario = input('Nome do usuário: ')
senha = input('Nome da senha: ')

usuario_bd = 'Pedro'
senha_bd = '123'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado')
else:
    print('Você não está logado')