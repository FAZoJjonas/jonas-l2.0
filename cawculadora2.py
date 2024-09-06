print('cawculadora...')
print('1 - adição')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
opção = int(input('escolha uma opção: '))
num1 = float(input('Escolha um numero'))
num2 = float(input('Escolha o segundo numero'))

if opção == 1:
    print(num1 + num2)
elif opção == 2:
    print(num1 - num2)
elif opção == 3:
    print(num1 * num2)
else:
    if num2 != 0:
        print(num1 / num2)
    else:
        print('você é idiota e burro')