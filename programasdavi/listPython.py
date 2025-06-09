from random import randint

minhaLista = ['Elielza','Jhuly', 'Vitória','Evilyn','Elizangela','Jinx']
n = 1
for i in minhaLista:
    print(f'{n}. {i}')
    n += 1
    
print('-'*20)

print(f'A primeira pessoa da minha lista é a: {minhaLista[0]}')
print(f'A segunda pessoa da minha lista é a: {minhaLista[1]}')
print(f'A ultima pessoa da minha lista é a: {minhaLista[5]}')

print('-'*20)

for i in range(0, len(minhaLista)):
    print(f'A {i+1}° pessoa da minha lista é a: {minhaLista[i]}')

print('-'*20)

print(minhaLista[::2])
print(minhaLista[1::2])

print('-'*20)

print(f'Randomizado aparece é aaaaaaaaaa: {minhaLista[randint(1,5)]}')
print(f'Quem eu quero ????? \n{minhaLista[1]}')

print('-'*20)

minhaLista.append('Esashika')
print(f'Nome dela: \n{minhaLista[1]} {minhaLista[6]}')

print('-'*20)

minhaLista.sort()
print(minhaLista)

print('-'*20)

minhaLista.reverse()
print(minhaLista)
