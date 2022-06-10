from socket import if_indextoname


print("**********", end="\n")
print("Bem", "Vindo!", sep=" ", end="\n")
print("**********", end="\n")

nome = str(input("Digite seu nome: "))
numero = int(input("Digitea sua idade: "))
calculo = (numero % 2)
crianca = numero < 12
adolecente = numero < 18
adulto = numero < 60
ano = 2022
anoquenasceu = (ano - numero)

print("\n")
print("***************************************************", "\n")
print(" A sua idade é", numero, "anos e seu nome é", nome, "\n")

if(calculo == 0):
    print("", nome, "sua idade", numero, "é par", "\n")
else:
    print("", nome, "sua idade", numero, "é impar", "\n")

if(crianca):
    print(" Voce e crianca")
elif(adolecente):
    print(" Voce e adolecente")
elif(adulto):
    print(" Voce e adulto")
else:
    print(" Voce e Idoso")
print("\n", "Voce nasceu em", anoquenasceu, "\n")
print("***************************************************", "\n")
