for i in range(1,16):
    altura=float(input("Insira sua altura"))
    somaAltura += altura
    if i == 1:
        menorAltura = altura
        maiorAltura = altura
    elif altura < menorAltura:
        menorAltura = altura
    elif altura > maiorAltura:
        maiorAltura = altura

print(f"A menor altura do grupo é: {menorAltura}")
print(f"A maior altura do grupo é: {maiorAltura}")
print(f"A soma das altura do grupo é: {somaAltura}")