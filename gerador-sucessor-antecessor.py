num = int(input('Digite um número: '))

op = input('Deseja verificar o antecessor? (s/n) ')

if op == "s":
    antecessor = num - 1
    print('O antecessor de {} é: {}'.format(num, antecessor))

else:
    print('Parado.')

op = input('Deseja verificar o sucessor? (s/n) ')

if op == 's':
    sucessor = num + 1
    print('O sucessor de {} é: {}'.format(num,sucessor))

else:
    print('Parado.')