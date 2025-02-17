print("Bem vindo ao sistema")
qntPaoFrances=int(input("Quantos pães franceses vendeu hoje?"))
qntBroa=int(input("Quantas broas vendeu hoje?"))

totalPaoFrances = qntPaoFrances * 0.12
totalBroa = qntBroa * 1.50

TotalDeVendas= totalPaoFrances + totalBroa
qntDeveGurdPoupanca = TotalDeVendas / 10

print(f"Hoje você arrecadou R$ {TotalDeVendas}, deve guardar na poupança R$ {qntDeveGurdPoupanca}")