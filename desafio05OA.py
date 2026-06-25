try:
    n = int(input('Coloque um número: '))

    s = n + 1
    a = n -1

    print('O numero inteiro é {} e o numero susessor dele é {} e o antecessor é {}'.format(n, s, a))

except ValueError:
    print('Erro: O valor digitado não é um número inteiro válido.')