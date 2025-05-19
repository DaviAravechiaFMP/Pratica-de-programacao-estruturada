for i in range(1,6):
    valorA=int(input("Insira um número, vamos ver se ele é positivo ou negativo"))
    if valorA > 0:
        print(f'O número {valorA} é positivo')
    elif valorA < 0:
        print(f'O número {valorA} é negativo')
    else:
        print(f"O número {valorA} é neutro")