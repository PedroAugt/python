"""
Inicio de teste com variáveis
"""
var_nome = 'Pedro Augusto'
var_idade = 22  # int
altura = 1.70  # Float
e_maior = var_idade > 18  # bool
peso = 80

imc = peso / (altura * altura)
print(var_nome, 'tem', var_idade, 'e seu imc é', imc)
