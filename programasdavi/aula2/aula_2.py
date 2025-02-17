# Meu primeiro programa
# Exemplos de saida de dados
'''
print("1) Olá, mundo!!! Bem Vindo!!")
print("2) Olá, mundo!!!\nBem Vindo!!")
print("3) Olá, mundo!!!")
print("3)Bem vindo!!")
'''

# Exercicio 1
# Meu primeiro Programa
'''
identificador { nome =
palavra utilizada na declaração de variável
'''
'''
VARIÁVEIS
.Representam espaços na memória para armazenar valores
.Iniciar com letra
.Sem espaços
.Sem acentos
.Sem carácter especial, mas pode conter_.
.Não pode ser igual a palavras reservadas
'''
# idade = 15
# nome = "Maria"
# altura = 1.62
'''
= significa ATRIBUIR ( baseado na literatura)
15 foi atribuido a variável idade
idade recebe 15
'''
# print(idade)

# print(type(idade))
# print(nome)
# print(type(nome))
# print(altura)
# print(type(altura))

# print(idade,",",altura)
# print(type(idade),type(altura))
# print(nome)
# print(type(nome))

'''
Trabalhando com INPUT
'''

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("informe sua altura"))

print(nome, "tem", idade, "anos e mede", altura, ".")