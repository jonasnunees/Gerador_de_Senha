from random import sample


def mostrar_senha():
    for i in senha:
        print(i, end='')


caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'X', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '!', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '<', '>', ',', '.', ':', '?', '/']


quantidade = int(input('Informe a quantidade de caractereres que sua senha deve ter: '))


senha = sample(caracteres, quantidade)


mostrar_senha()