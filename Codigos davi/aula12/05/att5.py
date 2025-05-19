from random import randint

votosCandidato1 = 0
votosCandidato2 = 0
votosCandidato3 = 0
votosCandidato4 = 0
votosNulos = 0
votosBrancos = 0
for i in range(1,101):
    # valor = int(input("Insira o seu voto"))
    valor = randint(1,6)
    if valor == 1:
        print("Votou em Lucas")
        votosCandidato1 += 1
    elif valor == 2:
        print("Votou em Will")
        votosCandidato2 += 1
    elif valor == 3:
        print("Votou em Siguel")
        votosCandidato3 += 1
    elif valor == 4:
        print("Votou em Vitor")
        votosCandidato4 += 1
    elif valor == 5:
        print("Votou nulo")
        votosNulos += 1
    elif valor == 6:
        print("Voto em branco")
        votosBrancos += 1
    else:
        print('Valor inválido')

print(f'O candidato Lucas teve {votosCandidato1} votos')
print(f'O candidato Will teve {votosCandidato2} votos')
print(f'O candidato Siguel teve {votosCandidato3} votos')
print(f'O candidato Vitor teve {votosCandidato4} votos')
print(f'Tiveram {votosNulos} votos nulos')
print(f'Tiveram {votosBrancos} votos em branco')