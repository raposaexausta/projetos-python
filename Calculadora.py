#Este código foi feito usando while true porque cria um laço infinito
#O programa roda continuamente até que o user encerre
#Se algo inválido for digitado, o continue faz o laço recomeçar do início
#Evita que o programa termine por erro e permite novas tentativas sem precisar reiniciar o script.

while True:
    num1 = input ('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-*/): ')


    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except:
        print('Digite um número válido ')
        continue

    operadores_validos = '+=*/'

    if operador not in operadores_validos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando conta; Confira o resultado: ')
    if operador == '+':
        print(f'{num1_float} + {num2_float} = ', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float} - {num2_float} = ', num1_float - num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float} = ', num1_float * num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float} = ', num1_float / num2_float)


    sair = input("Deseja sair? ").lower().startswith('s')

    if sair is True:
        break



