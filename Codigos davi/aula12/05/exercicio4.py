multip = int(input("Você deseja a tabuada de qual número?"))
maxValor = int(input("Você deseja a tabuada até qual valor?"))

for i in range (1, maxValor+1):
    valor = i * multip 
    print(f'{i} X {multip} = {valor}')