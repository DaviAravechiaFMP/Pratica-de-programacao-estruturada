# Exercício:

# Uma rainha requisitou os serviços de um monge, o qual exigiu o pagamento em grãos de trigo da seguinte maneira: os grãos de trigo seriam dispostos em um tabuleiro de xadrez, de tal forma que a primeira casa do tabuleiro tivesse um grão, e as casas seguintes o dobro da anterior. Construa um algoritmo que calcule quantos grãos de trigo a Rainha deverá pagar ao monge. Um tabuleiro tem 64 casas.
graos = 1
multTabul = 2
graosTotal = 1
for i in range(1, 64):
    graos *= multTabul
    graosTotal += graos
    multTabul*2
print(graosTotal)
    