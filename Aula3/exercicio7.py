diaDeHoje = int(input("Insira o dia de hoje"))
mesAtual= int(input("Insira o mês atual"))

diasMesesAtuais = (mesAtual -1) * 30

qntdDiasPassaram = diasMesesAtuais + diaDeHoje
print(f"Se passaram {qntdDiasPassaram} dias")