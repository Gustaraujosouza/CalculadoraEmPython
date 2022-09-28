while True:
    print()
    num_1 = float(input('Digite um numero (ou peso): '))
    num_2 = float(input('Digite outro numero (ou altura): '))
    operador = input('Digite um operador (ou imc se quiser saber o seu indice de massa corporea): ')

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '%':
        print(num_1 % num_2)
    elif operador == 'imc':
        print('{:.2f}' .format(num_1 / num_2 ** 2))
    else:
        print('Operador invalido!')

    sair = input('Deseja sair? [s]im ou [n]ao: ')

    if sair == 's':
        break
