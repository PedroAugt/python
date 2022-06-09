from socket import if_indextoname


print("**********", end="\n")
print("Bem", "Vindo!", sep=" ", end="\n")
print("**********", end="\n")

nome = str(input("Digite seu nome: "))
numero = int(input("Digite um numero: "))
print("O numero que", nome, "escolheu foi: ", numero)

calculo = (numero % 2)
if(calculo == 0):
    print("O numero", numero, "é par")
else:
    print("O numero", numero, "é impar")
