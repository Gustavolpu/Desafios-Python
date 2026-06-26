n = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: {type(n)}')

print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'Contem apenas números? {n.isdigit()}')
print(f'Contem apenas letras? {n.isalpha()}')
print(f'O texto é alfanumerico? {n.isalnum()}')
print(f'Contém letra maisculá? {n.isupper()}')
print(f'Contém letra minuscula? {n.islower()}')