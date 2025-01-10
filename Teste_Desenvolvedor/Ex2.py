numero = int(input('Informe um número para verificar se pertence à sequência de Fibonacci: '))

antecessor = 0
sucessor = 1
soma = 0
pertence = False
1
while soma <= numero:
    if soma == numero:
        pertence = True
        break
    antecessor = sucessor
    sucessor = soma
    soma = antecessor + sucessor

if pertence:
    print(f'O número {numero} pertence à sequência de Fibonacci.')
else:
    print(f'O número {numero} NÃO pertence à sequência de Fibonacci.')