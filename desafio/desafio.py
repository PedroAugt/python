''''
* criar variáveis para nome (str), idade (int);
* altura (float) e peso (float) de uma pessoa
* criar variável com ano atual (int)
* obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* exibir um texto com todos os valores na tela usado o f-string (com as chaves)
'''

nome = 'Pedro'
idade = 22
altura = 1.70
peso = 75
ano_atual = 2022
ano_nascimento = (ano_atual - idade)
imc = peso / (altura * altura)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')