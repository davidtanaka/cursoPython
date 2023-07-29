original = float(input('Preço do produto: '))
pagamento = int(input('Escolha a forma de pagametno desejado: \n'
                      f'1. à vista dinheiro (10% desconto)\n'
                      f'2. à vista cartão (5% desconto)\n'
                      f'3. 2x no cartão\n'
                      f'4. 3x ou mais no cartão (20% de juros)\n'
                      f'-> '))
if pagamento == 1:
    print(f'Total a pagar {original * 0.9}')
elif pagamento == 2:
    print(f'Total a pagar {original * 0.95}')
elif pagamento==3:
    print(f'2 parcelas no valor de {original / 2: .2f}')
else:
    parcela = int(input('Em quantas vezes quer pagar?: '))
    print(f'Em {parcela} vezes ficaria {original / parcela: .2f} por parcela')