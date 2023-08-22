import moedas

num = float(input('Digite o preco: R$'))

print(f"O valor digitado é de R${num:.2f}".replace('.',','))
print(f'A metade de R${num:.2f} é R${moedas.metade(num):.2f}'.replace('.',','))
print(f'O dobro de R${num:.2f} é R${moedas.dobro(num):.2f}'.replace('.',','))
print(f'Com aumento de 10% fica em R${moedas.aumentar(num, 10):.2f}'.replace('.',','))
print(f'Com reducao de 13% fica em R${moedas.diminuir(num, 13):.2f}'.replace('.',','))