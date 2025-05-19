# fatorial = int(input("Insira o valor que deseja o fatorial"))
# fatorialGuardado = fatorial
# for i in range(fatorial, 1, -1):
#     fatorial *= i-1
# print(f"O resultado do fatoria de {fatorial} é: {fatorialGuardado} ")

fatorial = int(input('Insira o valor que deseja saber o fatorial'))
fatorialGuardado = fatorial
exibirFator = str(fatorialGuardado) + "! = "
for i in range(fatorial, 1, -1):
    fatorial *= i-1
    exibirFator += str(i) + " x "
exibirFator += f'1 = {fatorial}'
print(exibirFator)
