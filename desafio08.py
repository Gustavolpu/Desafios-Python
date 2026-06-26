# === Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetro.

metros = float(input("Quantos metros tem: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f'{metros} metros equivalem a: ')
print(f'- {centimetros:.0f} centímetros')
print(f'- {milimetros:.0f} milímetros')

# :.0f na formatação: Como os resultados de centímetros e milímetros costumam ser números inteiros
# o :.0f serve para esconder os zeros depois da vírgula (ex: mostra 200 em vez de 200.0)

