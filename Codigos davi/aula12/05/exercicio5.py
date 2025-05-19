multip = int(input("Você deseja a tabuada de qual número?"))
minValor = int(input("Insira o valor em que a tabuada começa"))
maxValor = int(input("Insira o valor em que a tabuada termina"))

for i in range (minValor, maxValor+1):
    valor = i * multip 
    print(f'{i} X {multip} = {valor}')