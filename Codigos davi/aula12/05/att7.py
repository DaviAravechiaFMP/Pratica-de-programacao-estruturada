nomeCompl = input('Insira seu nome completo')

nomeHor = ""
for i in nomeCompl:
    if i == ' ':
        break
    nomeHor += i
    print(i)
print(nomeHor)