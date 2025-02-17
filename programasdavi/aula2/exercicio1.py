print("Bem vindo!!\nPor favor, realize o cadastro")
nome = str(input("Insira seu nome: "))
idade = input("Insira sua idade: ")
while not idade.isnumeric():
    print("Sua idade foi inserida incorretamente")
    idade = (input("Insira sua idade: "))
email = str(input("Insira seu gmail: "))
print(type(nome),type(idade),type(email))

print( nome != str)    
if nome.isalpha and email.isalpha:
        print("Seu cadastro foi realizado com sucesso")
else:
    print("Alguma informação não foi inserida corretamente")
    nome = (input("Insira seu nome: "))
    idade = (input("Insira sua idade: "))
    email = (input("Insira seu gmail: "))