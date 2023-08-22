import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é de {moedas.dobro(p)}')
print(f'Aumento 10%, temos {moedas.aumentando(p, 10)}')
print(f'Reduzindo 13%, temos {moedas.reduzindo(p, 13)}')