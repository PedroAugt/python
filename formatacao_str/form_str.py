
var_nome = 'Pedro Augusto'
var_idade = 22  # int
altura = 1.70  # Float
e_maior = var_idade > 18  # bool
peso = 80

imc = peso / (altura * altura)
print(var_nome, 'tem', var_idade, 'anos e seu imc é', imc)
print(f'{var_nome} tem {var_idade} anos e seu imc é {imc:.2f}')
print('{n} tem {a} anos e seu imc é {b}'.format(n = var_nome, a = var_idade, b = imc))
