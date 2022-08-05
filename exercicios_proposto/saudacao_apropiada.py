"""
Um programa que pergunta as horas para o usuário e faz a saudação apropiado para o horário
"""

hora = input('Poderia me informar as horas: ')
try:
    hora = float(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Erro!')
except:
    print('Digite apenas números!')
    print('Exemplos, 0 - 11, 12 - 17, 18 - 23')
    print('Utilize "." para se parar as horas dos minutos')